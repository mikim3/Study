// ./04fs/readfile-03.js

// 비동기방식을 좀더 간결하게 만들어보자
const fs = require('fs');

const file = fs.readFile('readme.txt',{
    encoding: 'utf8'
}, (err, file) => console.log(file)) 
//3번째 인자는 callback함수읨 자리고 그 자리에 익명함수를 선언해주면 좀더 간결한 코드작성이 가능하다.
// 추가로 리턴도 없기 때문에 {} 대괄호도 필요 없어 졌다.
