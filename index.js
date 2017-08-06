// Serve statics

var express = require('express');
var path = require('path');
var app = express()

// All static puts into ./static folder currently
app.use('/',express.static(path.join(__dirname, 'static')));

// index.html handler
app.get('/', function(req, res) {
    res.sendfile(path.join(__dirname, '/static/html/index.html'));
});

// profile.html handler
app.get('/profile', function(req, res) {
    res.sendfile(path.join(__dirname, '/static/html/profile.html'));
});

// publications.html handler
app.get('/publications', function(req, res) {
    res.sendfile(path.join(__dirname, '/static/html/publications.html'));
});

// publications.html handler
app.get('/award', function(req, res) {
    res.sendfile(path.join(__dirname, '/static/html/award.html'));
});
// server runs at :9111
var server = app.listen(9111, function () {
    var host = server.address().address;
    var port = server.address().port;
    console.log('Server running at ' + host + port);
});