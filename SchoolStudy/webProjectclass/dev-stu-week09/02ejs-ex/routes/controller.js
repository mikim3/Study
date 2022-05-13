// ./routes/controller.js
module.exports = function(app) {
    // app.get('/', (req, res) => {
    //     res.send('ROOT');
    // });

    // app.get('/contact', (req, res) => {
    //     res.send('Contact Us');
    // });

    app.get('/', (req, res) => {
        res.render('index.ejs');
    });

    app.get('/contact', (req, res) => {
        res.render('contact.ejs');
    });
};