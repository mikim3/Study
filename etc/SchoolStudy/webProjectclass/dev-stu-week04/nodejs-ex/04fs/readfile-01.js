// ./04fs/readfile-01.js

// 이것은 동기방식이다.
const fs = require('fs');
const file = fs.readFileSync('readme.txt',{
    encoding: 'utf8'
})

console.log(file); //파일내용을 읽어주세요
