// ./01httpserver/server_test1.js
var http = require('http');
var fs = require('fs');

var server = http.createServer( (req,res) => {
    fs.access('./images/house.jpg', (err) => {  //파일에 이경로에 접근한다.
        if(err) {  // 만약 오류면 아래 실행 
            res.statusCode = 404;
            res.end();
            return;
        }
        fs.readFile('./images/house.jpg', (err, data) => {  //에러가 아니라면 해당하는 데이터를 화면에 보여주세요 
            res.end(data);
        });
    });
}).listen(3000, () => {
    console.log('server on 3000 port');
});