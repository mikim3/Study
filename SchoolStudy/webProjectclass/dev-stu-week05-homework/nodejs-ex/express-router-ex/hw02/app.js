// ./express-router-ex/hw02/app.js
const express = require('express');
let app = express();

const hostname = '127.0.0.1';
const port = 3000;

// exports.module = users; 한것을 가져온다.
const users = require('./routes/users.js');
const board = require('./routes/board.js');

//app.use로 원하는 url에 원하는 js가 쓰이도록 설정 
app.use('/users',users);  /// 중요  이제 users를 사용할때 /users + users.js안에 경로로 접속한다.   
app.use('/boards',board);

app.listen(port, () => {
    console.log(`Express is running!!! on http://${hostname}:${port}/`);
});
