const express = require('express'),
    router = express.Router(),
    passport = require('passport'),
    User = require('../models/user'),
    Campground = require('../models/campground'),
    middleware = require('../middleware'),
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
    User.findOne({'username': req.params.username}, function(err, found_user){
        if(err || !found_user){
            console.log(err);
            req.flash('error', 'That user does not exist.');
            res.redirect('back');
        } else{
            Campground.find({'author.username': req.params.username}, function(err, campgrounds_from_database) {
                if (err) {
                    console.log(error);
                } else {
                    res.render('users/show', {
                        user: found_user,
                        campgrounds: campgrounds_from_database
                    });
                }
            });

        }
    });
});

// EDIT
router.get('/:username/edit', middleware.check_account_ownership, function(req, res) {
    User.findOne({'username': req.params.username}, function(err, found_user){
        if(err || !found_user){
            console.log(err);
            req.flash('error', 'That user does not exist.');
            res.redirect('back');
        } else{
            res.render('users/edit', {
                user: found_user
            });
        }
    });
});

// UPDATE
router.put('/:username', middleware.check_account_ownership, function(req, res) {
    if(!req.body.user.display_picture){
        req.body.user.display_picture = 'https://www.clipartkey.com/mpngs/m/152-1520367_user-profile-default-image-png-clipart-png-download.png';
    }
    User.updateOne({'username': req.params.username}, req.body.user, function(err, updated_user) {
        if (err) {
            req.flash('error', 'Update failed.')
            res.redirect('/users/' + req.params.username);
        } else {
            req.flash('success', 'Successfully updated!');
            res.redirect('/users/' + req.params.username);
        }
    });
});

module.exports = router;
