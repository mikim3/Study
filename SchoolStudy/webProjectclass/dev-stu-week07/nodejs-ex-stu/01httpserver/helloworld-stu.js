// ./01httpserver/helloWorld.js
var http = require('http');
// var server = http.createServer( (req, res) => {
//     res.write('Hello World');  //
//     res.end();  // write() 이후에는 반드시 end() 를 해야하고 안하면 나중에 문제가 생김
// });

var server = http.createServer(); //서버 객체에 서버를 시작
server.on('request', (req, res) => {
    res.write('Hello World');
    res.end();
});

server.listen(3000, () => {
    console.log('server on: 3000 port')
})

// server.listen(3000);