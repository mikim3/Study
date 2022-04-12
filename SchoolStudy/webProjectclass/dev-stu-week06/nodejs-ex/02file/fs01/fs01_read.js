// ./fs/file_read/fs01_read.js
const fs = require('fs')

// fs 모듈  
// fs: 파일에 데이터를 쓰고 읽어 올 수 있는 기능 제공



// 여기에 작성





fs.readFile('./test.txt', function(err, data){
    if(!err) {
        console.log('test.txt 파일읽기 성공')
        console.log(data)
        console.log(data.toString())
        return
    }
    console.log(err)
})
