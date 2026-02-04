@echo off
setlocal EnableExtensions

set "HERE=%~dp0"
for %%I in ("%HERE%..") do set "ROOT=%%~fI"

if not exist "%ROOT%\\judge.cmd" (
  echo [ERROR] Parent judge.cmd not found: %ROOT%\\judge.cmd
  pause
  exit /b 1
)

for %%I in ("%HERE%.") do set "PROBLEM=%%~nxI"
call "%ROOT%\\judge.cmd" "%PROBLEM%"
pause

