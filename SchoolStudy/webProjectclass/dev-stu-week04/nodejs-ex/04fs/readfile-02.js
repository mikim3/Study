// ./04fs/readfile-02.js

// 이것은 비동기방식이다.


const fs = require('fs');

const callback = (err, file) => {
    console.log(file);
}

const file = fs.readFile('readme.txt',{
    encoding: 'utf8'
}, callback)

// 위에 비동기로 file을 읽는중인데 log로 file 찍으라고 하면 undefined 라고 출력된다.
console.log(file); //파일내용을 읽어주세요
