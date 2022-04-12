// ./http/server1.js
const http = require('http');

http.createServer((req,res) => {
    res.write('Hello Node!');
    res.end();
}).listen(3000, () => {
    console.log('server on : 3000 port');
});
