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
        let weather_found = false;
        if (err || !found_campground) {
            console.log(err);
            req.flash('error', 'That campground does not exist.');
            res.redirect('/campgrounds');
        } else {
            // Project with _id: 0 was returning undefined. I have no idea why and it's driving me nuts
            User.find({}, {username: true}, function(err, all_available_users){
                users = []
                all_available_users.forEach(function(user){
                    users.push(user._id);
                });
                axios.get('http://api.openweathermap.org/data/2.5/weather?q=' + found_campground.location + '&appid=' + process.env['OPEN_WEATHER_MAP_API_KEY'])
                    .then(function(response) {
                        weather_found = true;
                        res.render('campgrounds/show', {
                            campground: found_campground,
                            users: users,
                            moment: moment,
                            weather: response.data
                        });
                    })
                    .catch(function(error) {
                        console.log(error);
                    })
                    .then(function(){
                        if(!weather_found){
                            res.render('campgrounds/show', {
                                campground: found_campground,
                                users: users,
                                moment: moment,
                            });
                        }
                });
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
// I realize the callback hell. I'll fix it in the future. Probably.
router.delete('/:id', middleware.check_campground_ownership, function(req, res) {
    Campground.findByIdAndRemove(req.params.id, function(err, removed_campground){
        if (err) {
            console.log(err);
        } else {
            User.update({_id: removed_campground.author.id}, {$inc: {'campgrounds_added': -1}}, function(err){
                if(err){
                    console.log(err);
                } else{
                    // doing this because filtering with _id: false to get only the author ids returned undefined
                    Review.find({_id: {$in: removed_campground.reviews}}, {author:{id: true}}, function(err, reviews_to_remove){
                        if (err) {
                            console.log(err);
                        } else{
                            const review_ids = []
                            reviews_to_remove.forEach(function(review){
                                review_ids.push(review.author.id);
                            })
                            review_ids.forEach(function(review_id){
                                User.update({_id: review_id}, {$inc: {'reviews_given': -1}}, function(err){
                                    if(err){
                                        console.log(err);
                                    }
                                });
                            });
                            Review.deleteMany({_id: {$in: removed_campground.reviews}}, function(err){
                                if(err){
                                    console.log(err);
                                } else{
                                    req.flash('success', 'Deleted campground.');
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
