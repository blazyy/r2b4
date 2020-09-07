const express = require('express'),
    router = express.Router(),
    passport = require('passport'),
    User = require('../models/user'),
    Campground = require('../models/campground'),
    async = require('async'),
    nodemailer = require('nodemailer'),
    crypto = require('crypto');

// INDEX
router.get('/', function(req, res) {
    User.find({}, function(err, users_from_database) {
        if (err) {
            console.log(error);
        } else {
            res.render('users/index', {
                users: users_from_database
            });
        }
    });
});

// NEW
router.get('/new', function(req, res) {
    res.render('users/new');
});

// CREATE
router.post('/', function(req, res) {
    let new_user = new User({
        username: req.body.username,
        email: req.body.email
    });
    User.register(new_user, req.body.password, function(err, new_user) {
        if (err) {
            console.log(err.keyValue);
            req.flash('error', err.message + "!");
            res.redirect('/users/new');
        } else {
            passport.authenticate('local')(req, res, function() {
                req.flash('success', 'Welcome to SpaceCamp, ' + new_user.username + "!");
                res.redirect('/campgrounds');
            });
        }
    });
});

// SHOW
router.get('/:username', function(req, res){
    User.find({'username': req.params.username}, function(err, found_user){
        console.log(found_user[0]);
        if(err || !found_user){
            console.log(err);
            req.flash('error', 'That user does not exist.');
            res.redirect('/users');
        } else{
            res.render('users/show', {
                user: found_user
            });
        }
    });
});

module.exports = router;
