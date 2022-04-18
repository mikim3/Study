// ./02getpost/reqres05.js
const http = require('http');

http.createServer( (req, res) => {
    let resData = '<html><body><h1>!!!!!hello world!!!!!</h1></body></html>'
    // res.writeHead(200, {'Content-Type': 'text/plain'});
    res.writeHead(200, {'Content-Type': 'text/html'});  // plain 이면 글자 그대로 html이면 html 해석해서 출력 
    res.end(resData);

}).listen(3000, () => {
    console.log('server on : 3000 port')
});
