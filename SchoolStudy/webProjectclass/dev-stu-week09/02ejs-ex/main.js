const express = require("express");
let app = express();
const ejs =  require("ejs");

app.set("view", __dirname, "views");
// app.set("view", __dirname, "views");
// app.set("view", __dirname, "views");

var router = require("./routes/controller")(app); //(app) app 객체가 있어야 된다.

var server = app.listen(3000, () => {
    console.log('server on port 3000');
})


