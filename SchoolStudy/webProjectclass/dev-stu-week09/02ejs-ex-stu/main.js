// ./main.js
const express = require('express');
let app = express();
const ejs = require('ejs');

app.set("views", __dirname + "/views");
app.set("view engine", "ejs");

var router = require('./routes/controller')(app);

const server = app.listen(3000, () =>  {
    console.log('server on port 3000');
});

