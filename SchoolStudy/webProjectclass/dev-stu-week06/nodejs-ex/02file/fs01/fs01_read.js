// ./fs/file_read/fs01_read.js
const fs = require('fs')


// 여기에 작성
fs.readFile('./test-stu.html',function(err, data) {
    if (!err){ //에러가 아닐때만 실행
        console.log('test.html 파일 읽기 성공');
        console.log(data) // 버퍼 내용이 나옴
        console.log(data.toString())
        return;
    }
    console.log(err)
})


fs.readFile('./test.txt', function(err, data){
    if(!err) {
        console.log('test.txt 파일읽기 성공')
        console.log(data)
        console.log(data.toString())
        return
    }
    console.log(err)
})
