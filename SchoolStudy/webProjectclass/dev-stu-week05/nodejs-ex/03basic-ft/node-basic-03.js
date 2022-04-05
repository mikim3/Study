// node-basid-03.js
// 블록킹 예제

function longRunningTask() {
  // 오래 걸리는 작업
  console.log('작업 끝');
}

console.log('시작');
longRunningTask();
console.log('다음 작업');

