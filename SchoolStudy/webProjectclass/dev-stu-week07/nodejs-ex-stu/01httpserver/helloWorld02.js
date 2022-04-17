// ./01httpserver/helloWorld02.js
var http = require('http');
var server = http.createServer();

server.on('request', function(req, res) {  // javascript에서는 이벤트를 등록할때 .on() 이라는 메서드에 등록한다. 
    res.write('Hello World');
    res.end();
});

server.listen(3000, () => {
    console.log('server on: 3000 port')
});