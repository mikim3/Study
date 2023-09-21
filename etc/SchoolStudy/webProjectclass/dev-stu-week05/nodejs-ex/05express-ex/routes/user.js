// ./routes/user.js
//  route는 mvc의 C컨트롤러와 유사하다. 

var express = require('express');
var router = express.Router(); // router 객체 생성

router.get('/:id', function(req, res) {
    res.send('Received a GET request, param:' + req.params.id);
});

router.post('/', function(req, res) {
    res.json({ success: true })
});

router.put('/', function(req, res) {
    res.status(400).json({ message: 'Hey, you. Bad Request!' });
});

router.delete('/', function(req, res) {
    res.send('Received a DELETE request');
});

module.exports = router;  //여기서 exports 하면 app.js에서 
// require('./routes/user'); 로 불러온다.
