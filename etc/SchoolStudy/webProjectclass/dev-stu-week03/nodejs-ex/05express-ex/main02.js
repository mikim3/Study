// main.js: 라우팅 (POSTMAN 사용하여 테스트)
var express = require('express');
var app = express();

app.get('/', function(req, res) {
    res.send('Hello World!! main2');
});

app.listen(3000, function() {
    console.log('Example App listening on port 3000');
});

app.get('/user/:id', function(req, res){
    res.send('Received a GET request, parma:' + req.params.id);
});

app.post('/user', function(req, res){
    res.json({ success: true})
});

app.put('/user', function(req, res){   //내용 전달 관련은 put 
    res.status(400).json({ message: 'Hey, you. Bad Requset!'});
});

app.delete('/user', function(req, res){
    res.send('Received a DELETE request');
});



