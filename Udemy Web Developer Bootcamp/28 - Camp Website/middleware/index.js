const Campground = require('../models/campground'),
    Review = require('../models/review'),
    User = require('../models/user');

const middleware_object = {
    check_campground_ownership: function(req, res, next) {
        if (req.isAuthenticated()) { // check is user is logged in
            Campground.findById(req.params.id, function(err, found_campground) {
                // !found_campground is important, without this the app will break if the user manually enters a random ID of the same length
                if (err || !found_campground) {
                    console.log(err);
                    req.flash('error', 'That campground does not exist.');
                    res.redirect('/campgrounds');
                } else {
                    // not using === because author.id is mongoose object and req.user._id is a string
                    if (found_campground.author.id.equals(req.user._id) || req.user.is_admin) { // does user own the campground?
                        next();
                    } else {
                        req.flash('error', 'You don\'t have permission to do that!');
                        res.redirect('/campgrounds/' + found_campground._id);
                    }
                }
            });
        } else {
            req.flash('error', 'You need to be logged in to do that!');
            res.redirect('/login');
        }
    },

    check_review_ownership: function(req, res, next) {
        if (req.isAuthenticated()) { // check is user is logged in
            Review.findById(req.params.review_id, function(err, found_review) {
                if (err || !found_review) {
                    console.log(err);
                    req.flash('error', 'That review does not exist.');
                    res.redirect('/campgrounds/' + req.params.id);
                } else {
                    // not using === because author.id is mongoose object and req.user._id is a string
                    if (found_review.author.id.equals(req.user._id) || req.user.is_admin) { // does user own the review?
                        next();
                    } else {
                        req.flash('error', 'You don\'t have permission to do that!');
                        res.redirect('back');
                    }
                }
            });
        } else {
            req.flash('error', 'You need to be logged in to do that!');
            res.redirect('back');
        }
    },

    check_account_ownership: function(req, res, next) {
        if (req.isAuthenticated()) { // check is user is logged in
            User.findOne({'username': req.params.username}, function(err, found_user) {
                if (err || !found_user) {
                    console.log(err);
                    req.flash('error', 'That user does not exist.');
                    res.redirect('back');
                } else {
                    // not using === because user._id is mongoose object and req.user._id is a string
                    if (found_user._id.equals(req.user._id) || req.user.is_admin) { // does user own the profile?
                        next();
                    } else {
                        req.flash('error', 'You don\'t have permission to do that!');
                        res.redirect('/users/' + req.params.username);
                    }
                }
            });
        } else {
            req.flash('error', 'You need to be logged in to do that!');
            res.redirect('/login');
        }
    },

    is_logged_in: function(req, res, next) {
        if (req.isAuthenticated()) {
            return next();
        }
        req.flash('error', 'You need to be logged in to do that!'); // this line HAS TO BE BEFORE REDIRECT. this doesn't show up on current page, it shows up on the next page, i.e. here it'll show up in /login below
        res.redirect('/login');
    }
};

module.exports = middleware_object;
