// ./file/fs.js
// fs 모듈  
// fs: 파일에 데이터를 쓰고 읽어 올 수 있는 기능 제공

var fs = require('fs');

// 이러면 무조건 1이 먼저 나올꺼 같지만 순서가 랜덤하게 나온다. 원래 비동기의 순서는 보장 받지 못한다.
// fs.writeFile('data1.txt', 'Hello Node.js 01', function(error){
//     console.log('비동기식 저장1');
// });
// fs.writeFile('data2.txt', 'Hello Node.js 02', function(error){
//     console.log('비동기식 저장2');
// });

// fs.appendFile() 은 내용을 추가한다.
// fs.appendFile('data1.txt', ' 안녕하세요', function(error){
// 	console.log("비동기식 추가1");
// });
// fs.appendFile('data2.txt', ' 반갑습니다', function(error){
// 	console.log("비동기식 추가2");
// });

// 파일의 내용을 읽어 들인다.   기본적으로 버퍼로 보여줘서 그냥 실행하면 이상한 값 나오고 .toString()을 붙여야 읽을수 있다.
// fs.readFile('data1.txt', function(error, data){
// 	console.log("data1: ", data.toString());
// });
// fs.readFile('data2.txt', function(error, data){
// 	console.log("data2: ", data.toString());
// });


// 순서 지킴
// fs.writeFileSync("data3.txt", "Hello node.js 03");
// console.log("동기식 저장 1");

// fs.writeFileSync("data4.txt", "Hello node.js 04");
// console.log("동기식 저장 2");

//
// fs.appendFileSync("data3.txt", " 안녕하세요");
// console.log("파일 내용 추가 1");

// fs.appendFileSync("data4.txt", " 반갑습니다");
// console.log("파일 내용 추가 2");

// var data3 = fs.readFileSync("data3.txt");
// console.log("data3 :", data3.toString());

// var data4 = fs.readFileSync("data4.txt");
// console.log("data4 :", data4.toString());
