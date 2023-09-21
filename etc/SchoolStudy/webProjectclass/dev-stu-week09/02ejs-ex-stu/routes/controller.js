// ./routes/controller.js
module.exports = function(app) {
    app.get('/', (req, res) => {
        // var html = "<!DOCTYPE HTML>"
        //     + "<html>"
        //     + "<head>"
        //     + "<meta charset='UTF-8'>"
        //     + "<title>"
        //     + "</title>"
        //     + "<body>"
        //     + "<h1>ROOT</h1>"
        //     + "</body>"
        //     + "</html>"
        // res.render(html);
        res.render('index.ejs');
        // res.send('ROOT');
    });
    // app.get('/contact', (req, res) => {
    //     res.send('Contact Us');
    // });
    app.get('/contact', (req, res) => {
        // res.send('Contact Us');
        res.render('contact.ejs');
    });
}