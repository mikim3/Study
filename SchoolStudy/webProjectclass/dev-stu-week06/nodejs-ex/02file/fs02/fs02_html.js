// ./fs/file_read/fs02_html.js
const fs = require('fs')
const http = require('http');

http.createServer((req, res) => {
    fs.readFile('./test.html', (err, data) => {
        if(!err){
            //text/plain을 주면 글자그대로를읽고 html을 주면 html파일로읽음
            res.writeHead(200, {'Content-Type': 'text/html; charset=utf-8'})
            // res.writeHead(200, {'Content-Type': 'text/plain; charset=utf-8'}) 
            res.end(data)
            return
        }
        res.writeHead(500)
        res.end('서버에 문제가 발생했습니다.')
    })
}).listen(3000, () => {
    console.log('server on : 3000 port')
})
