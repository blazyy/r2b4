const express = require('express'),
    router = express.Router(),
    Campground = require('../models/campground'),
    middleware = require('../middleware'),
    moment = require('moment'),
    axios = require('axios');;

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
    req.flash('error', 'You don\'t have permission to do that!')
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
            User.update({_id: req.user._id}, {$inc: {'campgrounds_added': 1}}, function(err, updated_campground){
                if(err){
                    console.log(err);
                } else{
                    res.redirect('/campgrounds');
                }
            });
        }
    });
});

// SHOW
router.get('/:id', function(req, res) {
    // The .populate('reviews').exec() here just replaces the review references with the actual content
    // of the reviews themselves so that these can be sent as an object to the /show.js page
    Campground.findById(req.params.id).populate('reviews').exec(function(err, found_campground) {
        if (err || !found_campground) {
            console.log(err);
            req.flash('error', 'That campground does not exist.');
            res.redirect('/campgrounds');
        } else {
            axios.get('http://api.openweathermap.org/data/2.5/weather?q=' + found_campground.location + '&appid=' + process.env['OPEN_WEATHER_MAP_API_KEY'])
                .then(function(response) {
                    res.render('campgrounds/show', {
                        campground: found_campground,
                        moment: moment,
                        weather: response.data
                    });
                })
                .catch(function(error) {
                    console.log(error);
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
    Campground.findByIdAndUpdate(req.params.id, req.body.camp, function(err, updated_campground) {
        if (err) {
            res.redirect('/campgrounds');
        } else {
            res.redirect('/campgrounds/' + req.params.id);
        }
    });
});

// DELETE
router.delete('/:id', middleware.check_campground_ownership, function(req, res) {
    Campground.findByIdAndRemove(req.params.id, function(err, removed_campground){
        if (err) {
            console.log(err);
        } else {
            Review.deleteMany({_id: {$in: removed_campground.reviews}}, function(err){
                if (err) {
                    console.log(err);
                } else{
                    User.update({_id: req.user._id}, {$inc: {'campgrounds_added': -1}}, function(err, updated_campground){
                        if(err){
                            console.log(err);
                        } else{
                            User.updateMany({$inc: {'reviews_given': -1}}, function(err){
                                if(err){
                                    console.log(err);
                                } else{
                                    res.redirect('/campgrounds');
                                }
                            });
                        }
                    });
                }
            });
        }
    })
});

module.exports = router;
