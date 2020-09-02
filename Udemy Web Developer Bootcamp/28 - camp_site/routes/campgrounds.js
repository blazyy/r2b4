const express = require('express'),
    router = express.Router(),
    Campground = require('../models/campground'),
    middleware = require('../middleware'),
    moment = require('moment');

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
router.get('/new', middleware.is_logged_in, function(req, res) {
    res.render('campgrounds/new');
});

// CREATE - campground
router.post('/', middleware.is_logged_in, function(req, res) {
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
        if (err || !found_campground) {
            console.log(err);
            req.flash('error', 'That campground does not exist.');
            res.redirect('/campgrounds');
        } else {
            // console.log(mapboxgl);
            res.render('campgrounds/show', {
                campground: found_campground,
                moment: moment,
            });
        }
    });
});

// EDIT
router.get('/:id/edit', middleware.check_campground_ownership, function(req, res) {
    Campground.findById(req.params.id, function(err, found_campground) {
        if (err || !found_campground) {
            console.log(err);
            req.flash('error', 'That campground does not exist.');
            res.redirect('/campgrounds');
        } else {
            res.render('campgrounds/edit', {
                campground: found_campground
            });
        }
    });
});

// UPDATE
router.put('/:id', middleware.check_campground_ownership, function(req, res) {
    Campground.findByIdAndUpdate(req.params.id, req.body.camp, function(err, update_campground) {
        if (err) {
            res.redirect('/campgrounds');
        } else {
            res.redirect('/campgrounds/' + req.params.id);
        }
    });
});

// DELETE
router.delete('/:id', middleware.check_campground_ownership, function(req, res) {
    Campground.findByIdAndRemove(req.params.id, (err, removed_campground) => {
        if (err) {
            console.log(err);
        }
        Comment.deleteMany( {_id: { $in: removed_campground.comments } }, (err) => {
            if (err) {
                console.log(err);
            }
            res.redirect("/campgrounds");
        });
    })
});

module.exports = router;
