// ./fs/fs_refilejs
var fs = require('fs');


// fs.readFile()은 비동기   fs.readFileSync는 동기 방식이다.
// fs.readFile(읽을 파일명,인코딩형식??,function(에러시동작함수, 읽은 파일 데이터 )
console.log('A');
fs.readFile('sample.txt', 'utf8', function (err, result) {
    console.log(result);
});
console.log('C');
