// ./fileupload/singleserver.js
const fs = require('fs');
const express = require('express');
const multer = require('multer');

let upload = multer( { dest: './uploads'})
let app = express();


app.get('/single' , (req, res) => {
    fs.readFile('single.html', 'utf8', (err, data) => {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.end(data);
    });
});

// app.post('form태그 action')
// upload.single('input태그에 name속성')
app.post('/singleupload' , upload.single('file'), (req, res) => { 
    console.log(req.body)
    console.log(req.file)
    res.status(204).end()
});





app.listen(3000, () => {
    console.log('server on 3000 port')
});
