const express = require('express'),
    router = express.Router(),
    passport = require('passport'),
    User = require('../models/user');

router.get('/', function(req, res) {
    res.render('landing');
});

// Register
router.get('/register', function(req, res){
    res.render('register');
});

router.post('/register', function(req, res){
    let new_user = new User({username: req.body.username});
    User.register(new_user, req.body.password, function(err, new_user){
        if(err){
            console.log(err);
        }
        else{
            passport.authenticate('local')(req, res, function(){
                res.redirect('/campgrounds');
            });
        }
    });
});

router.get('/login', function(req, res){
    res.render('login');
});

// passport.authenticate() is the middleware
router.post('/login', passport.authenticate('local', {
    successRedirect: '/campgrounds',
    failureRedirect: '/login'
}));

router.get('/logout', function(req, res){
    req.logout();
    res.redirect('/campgrounds');
});

// CREATE - comment
router.get('*', function(req, res) {
    res.sendStatus(404);
});

function isLoggedIn(req, res, next){
    if(req.isAuthenticated()){
        return next();
    }
    res.redirect('/login');
}

module.exports = router;
