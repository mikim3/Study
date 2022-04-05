// app.js
const express = require('express');
const app = express();

const hostname = '127.0.0.1';
const port = 3000;

app.get('/', (req, res) => {
    res.send('<H1>Hello World!</H1>');
});

app.get('/sayhello/:name', (req, res) => {
    res.status(200);   //상태가 200
    let name = req.params.name;  // 해당하는 변수의 name 값을 저장하는데 
    res.send(`Hello, ${name} `);  //  '' 가 아니라 `` 이다 조심하자
});


// app.get('/', (req, res) => {
//     res.send('Hello World!');
// });

// 다음 문장 추가
app.get('/sayhello/:name', (req, res) => {
    res.status(200);
    let name = req.params.name;
 
    res.send(`<h1>Hello, ${name}`);
 });

app.listen(port, () => {
    console.log(`Express is running on http://${hostname}:${port}/`);
} );

// app.listen(port, () => {
//     console.log(`Express is running on localhost:3000`);
// } );
