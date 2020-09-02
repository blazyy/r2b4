const Campground = require('../models/campground'),
    Comment = require('../models/comment');

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
                    if (found_campground.author.id.equals(req.user._id)) { // does user own the campground?
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

    check_comment_ownership: function(req, res, next) {
        if (req.isAuthenticated()) { // check is user is logged in
            Comment.findById(req.params.comment_id, function(err, found_comment) {
                if (err || !found_comment) {
                    console.log(err);
                    req.flash('error', 'That comment does not exist.');
                    res.redirect('/campgrounds/' + req.params.id);
                } else {
                    // not using === because author.id is mongoose object and req.user._id is a string
                    if (found_comment.author.id.equals(req.user._id)) { // does user own the comment?
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

    is_logged_in: function(req, res, next) {
        if (req.isAuthenticated()) {
            return next();
        }
        req.flash('error', 'You need to be logged in to do that!'); // this line HAS TO BE BEFORE REDIRECT. this doesn't show up on current page, it shows up on the next page, i.e. here it'll show up in /login below
        res.redirect('/login');
    }
};

module.exports = middleware_object;
