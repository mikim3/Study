
const http = require('http');


// http의 res 객체 res.writeHead : 응답에 대한 정보기록, header정보
// res.write 클라이언트에 보낼 데이터, body  
// res.end   응답종료
http.createServer((req,res) =>{
    res.writeHead(200, {'Content-type': 'text/html; charset=utf-8'});
    res.write('<h1>Hello Node!</h1>');
    res.end('<p>Hello Server</p>');
}).listen(3000, () => {
    console.log('Server on : 3000 port');
})
