const express = require('express'),
    router = express.Router();

require('dotenv').config({path: 'requires.env'});

router.get('/', function(req, res) {
    res.render('landing');
});

router.get('*', function(req, res) {
    res.sendStatus(404);
});

module.exports = router;
