#!/usr/bin/env python3
from __future__ import annotations

import argparse
import difflib
import os
import re
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Case:
    number: int
    input_path: Path
    output_path: Path


@dataclass(frozen=True)
class CaseRun:
    case: Case
    status: str  # PASS | WA | TLE | RE
    elapsed_s: float
    message: str = ""


def _normalize_newlines(text: str) -> str:
    return text.replace("\r\n", "\n").replace("\r", "\n")


def normalize_output_loose(text: str) -> str:
    text = _normalize_newlines(text)
    lines = [line.rstrip(" \t") for line in text.split("\n")]
    while lines and lines[-1] == "":
        lines.pop()
    return "\n".join(lines)


def normalize_output_strict(text: str) -> str:
    return _normalize_newlines(text)


def discover_cases(problem_dir: Path) -> list[Case]:
    inputs: dict[int, Path] = {}
    outputs: dict[int, Path] = {}

    for path in problem_dir.glob("in*.txt"):
        match = re.fullmatch(r"in(\d+)\.txt", path.name)
        if match:
            inputs[int(match.group(1))] = path

    for path in problem_dir.glob("out*.txt"):
        match = re.fullmatch(r"out(\d+)\.txt", path.name)
        if match:
            outputs[int(match.group(1))] = path

    numbers = sorted(set(inputs) & set(outputs))
    return [Case(n, inputs[n], outputs[n]) for n in numbers]


def discover_problem_dirs(root: Path) -> list[Path]:
    candidates: list[Path] = []
    for child in root.iterdir():
        if not child.is_dir():
            continue
        if not (child / "AA.py").is_file():
            continue
        if discover_cases(child):
            candidates.append(child)
    return sorted(candidates, key=lambda p: p.name)


def run_python(
    solution_path: Path,
    *,
    input_text: str,
    timeout_s: float,
    cwd: Path,
) -> tuple[str, str, int | None, float, bool]:
    cmd = [sys.executable, str(solution_path)]
    start = time.perf_counter()
    try:
        proc = subprocess.run(
            cmd,
            input=input_text,
            capture_output=True,
            text=True,
            cwd=str(cwd),
            timeout=timeout_s,
            env={**os.environ, "PYTHONUNBUFFERED": "1"},
        )
        elapsed = time.perf_counter() - start
        return proc.stdout, proc.stderr, proc.returncode, elapsed, False
    except subprocess.TimeoutExpired as exc:
        elapsed = time.perf_counter() - start
        stdout = exc.stdout if isinstance(exc.stdout, str) else (exc.stdout or b"").decode(errors="replace")
        stderr = exc.stderr if isinstance(exc.stderr, str) else (exc.stderr or b"").decode(errors="replace")
        return stdout, stderr, None, elapsed, True


def unified_diff(expected: str, actual: str) -> str:
    expected_lines = expected.splitlines(keepends=True)
    actual_lines = actual.splitlines(keepends=True)
    diff = difflib.unified_diff(
        expected_lines,
        actual_lines,
        fromfile="expected",
        tofile="actual",
    )
    return "".join(diff)


def read_text_smart(path: Path) -> str:
    data = path.read_bytes()
    if data.startswith(b"\xff\xfe") or data.startswith(b"\xfe\xff"):
        return data.decode("utf-16")
    if data.startswith(b"\xef\xbb\xbf"):
        return data.decode("utf-8-sig")
    try:
        return data.decode("utf-8")
    except UnicodeDecodeError:
        try:
            return data.decode("cp949")
        except UnicodeDecodeError:
            return data.decode(errors="replace")


def grade_problem(
    problem_dir: Path,
    *,
    solution_path: Path,
    timeout_s: float,
    strict: bool,
    show_diff: bool,
) -> tuple[list[CaseRun], float, float]:
    cases = discover_cases(problem_dir)
    if not cases:
        raise SystemExit(f"테스트케이스를 찾지 못했습니다: {problem_dir}")

    normalize = normalize_output_strict if strict else normalize_output_loose

    runs: list[CaseRun] = []
    total = 0.0
    max_elapsed = 0.0

    for case in cases:
        input_text = read_text_smart(case.input_path)
        expected_text = read_text_smart(case.output_path)

        stdout, stderr, returncode, elapsed, timed_out = run_python(
            solution_path,
            input_text=input_text,
            timeout_s=timeout_s,
            cwd=problem_dir,
        )

        total += elapsed
        max_elapsed = max(max_elapsed, elapsed)

        if timed_out:
            runs.append(
                CaseRun(
                    case=case,
                    status="TLE",
                    elapsed_s=elapsed,
                    message=f"timeout({timeout_s:.3f}s)",
                )
            )
            continue

        if returncode != 0:
            msg = f"exit={returncode}"
            if stderr.strip():
                msg += f"\n{stderr.rstrip()}"
            runs.append(CaseRun(case=case, status="RE", elapsed_s=elapsed, message=msg))
            continue

        norm_expected = normalize(expected_text)
        norm_actual = normalize(stdout)
        if norm_expected == norm_actual:
            runs.append(CaseRun(case=case, status="PASS", elapsed_s=elapsed))
            continue

        msg = ""
        if show_diff:
            msg = unified_diff(norm_expected + "\n", norm_actual + "\n").rstrip()
        runs.append(CaseRun(case=case, status="WA", elapsed_s=elapsed, message=msg))

    return runs, total, max_elapsed


def _fmt_s(seconds: float) -> str:
    if seconds < 1:
        return f"{seconds * 1000:.1f}ms"
    return f"{seconds:.3f}s"


def _collect_runs(runs: list[CaseRun]) -> tuple[int, int]:
    passed = sum(1 for r in runs if r.status == "PASS")
    return passed, len(runs)


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(
        description="WSL/Windows 겸용 Python 채점기 (in*.txt/out*.txt 비교 + 실행시간 측정)",
    )
    parser.add_argument(
        "target",
        nargs="?",
        default=None,
        help="문제 폴더(예: '1. k번째 약수') 또는 풀이 파일 경로(예: '1. k번째 약수/AA.py'). 비우면 자동 탐색.",
    )
    parser.add_argument(
        "--file",
        default="AA.py",
        help="문제 폴더 안에서 실행할 풀이 파일명 (기본: AA.py)",
    )
    parser.add_argument("--timeout", type=float, default=3.0, help="케이스당 제한시간(초) (기본: 3.0)")
    parser.add_argument("--strict", action="store_true", help="공백/개행까지 최대한 엄격 비교 (CRLF는 자동 보정)")
    parser.add_argument("--no-diff", action="store_true", help="오답 시 diff 출력 생략")
    parser.add_argument("--list", action="store_true", help="탐지된 문제 폴더 목록만 출력")
    parser.add_argument("--all", action="store_true", help="현재 폴더 아래 모든 문제 폴더 채점")

    args = parser.parse_args(argv)

    root = Path.cwd()
    show_diff = not args.no_diff

    # If we're already inside a problem directory, prefer that as default.
    if args.target is None and (root / args.file).is_file() and discover_cases(root):
        problem_dirs = [root]
    else:
        problem_dirs = discover_problem_dirs(root)

    if args.list:
        if not problem_dirs:
            print("문제 폴더를 찾지 못했습니다.")
            return 1
        for p in problem_dirs:
            print(p.name)
        return 0

    if args.target is not None:
        target_path = Path(args.target)
        if target_path.is_file() and target_path.suffix.lower() == ".py":
            solution_path = target_path.resolve()
            problem_dir = target_path.parent.resolve()
            problem_dirs = [problem_dir]
        else:
            problem_dir = target_path.resolve()
            problem_dirs = [problem_dir]
            solution_path = (problem_dir / args.file).resolve()
    else:
        solution_path = None

    if not problem_dirs:
        print("문제 폴더를 찾지 못했습니다. (예: 'python judge.py --list')")
        return 1

    if not args.all and args.target is None and len(problem_dirs) > 1:
        # Default behavior at root: run all, but tell the user how to run one.
        args.all = True

    overall_exit = 0
    overall_total = 0.0
    overall_max = 0.0
    overall_passed = 0
    overall_cases = 0

    for problem_dir in problem_dirs if args.all else problem_dirs[:1]:
        solution = solution_path or (problem_dir / args.file).resolve()
        if not solution.is_file():
            print(f"풀이 파일을 찾지 못했습니다: {solution}")
            overall_exit = 1
            continue

        runs, total, max_elapsed = grade_problem(
            problem_dir,
            solution_path=solution,
            timeout_s=args.timeout,
            strict=args.strict,
            show_diff=show_diff,
        )

        passed, total_cases = _collect_runs(runs)
        overall_passed += passed
        overall_cases += total_cases
        overall_total += total
        overall_max = max(overall_max, max_elapsed)

        print(f"\n== {problem_dir.name} ({solution.name}) ==")
        for run in runs:
            suffix = ""
            if run.status == "TLE":
                suffix = f" ({run.message})"
            print(f"[{run.status}] case {run.case.number}  {_fmt_s(run.elapsed_s)}{suffix}")
            if run.status in {"WA", "RE"} and run.message:
                print(run.message)
                print("-" * 60)
        print(f"summary: {passed}/{total_cases} passed | total {_fmt_s(total)} | max {_fmt_s(max_elapsed)}")

        if passed != total_cases:
            overall_exit = 1

    if args.all and overall_cases:
        print(
            f"\nALL summary: {overall_passed}/{overall_cases} passed | total {_fmt_s(overall_total)} | max {_fmt_s(overall_max)}"
        )

    return overall_exit


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
