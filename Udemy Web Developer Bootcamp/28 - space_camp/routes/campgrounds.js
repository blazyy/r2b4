const express = require('express'),
    router = express.Router(),
    Campground = require('../models/campground');

// INDEX
router.get('/', function(req, res) {
    Campground.find({}, function(err, campgrounds_from_database) {
        if (err) {
            console.log(error);
        } else {
            res.render('campgrounds/index', {
                campgrounds: campgrounds_from_database
            });
        }
    });
});

// NEW - campground
router.get('/new', isLoggedIn, function(req, res) {
    res.render('campgrounds/new');
});

// CREATE - campground
router.post('/', isLoggedIn, function(req, res) {
    let author = {
        id: req.user._id, // req.user from PassportJS
        username: req.user.username
    }
    req.body.camp['author'] = author;
    Campground.create(req.body.camp, function(err, new_campground) {
        if (err) {
            console.log(err);
        } else {
            res.redirect('/campgrounds');
        }
    });
});

// SHOW
router.get('/:id', function(req, res) {
    // The .populate('comments').exec() here just replaces the comment references with the actual content
    // of the comments themselves so that these can be sent as an object to the /show.js page
    Campground.findById(req.params.id).populate('comments').exec(function(err, found_campground) {
        if (err) {
            console.log(err);
        } else {
            res.render('campgrounds/show', {
                campground: found_campground
            });
        }
    });
});

function isLoggedIn(req, res, next){
    if(req.isAuthenticated()){
        return next();
    }
    res.redirect('/login');
}

module.exports = router;
