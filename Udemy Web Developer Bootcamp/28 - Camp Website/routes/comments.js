const express = require('express'),
    router = express.Router({mergeParams: true}), // to enable the req object to be read, if this option isn't specified then no objects will be passed
    Campground = require('../models/campground'),
    Comment = require('../models/comment'),
    middleware = require('../middleware'),
    moment = require('moment');

// NEW - comment
router.get('/new', middleware.is_logged_in, function(req, res){
    Campground.findById(req.params.id, function(err, found_campground){
        if (err || !found_campground) {
            console.log(err);
            req.flash('error', 'That campground does not exist.');
            res.redirect('/campgrounds');
        } else {
            res.render('comments/new', {campground: found_campground});
        }
    });
});

// CREATE - comment
router.post('/', middleware.is_logged_in, function(req, res){
    Campground.findById(req.params.id, function(err, found_campground){
        if(err){
            console.log(err);
        } else{
            Comment.create(req.body.comment, function(err, new_comment){
                if(err){
                    console.log(err);
                } else{
                    new_comment.author.id = req.user._id; // req.user from PassportJS? I think so.
                    new_comment.author.username = req.user.username;
                    new_comment.save();
                    found_campground.comments.push(new_comment);
                    found_campground.save();
                    req.flash('success', 'Added new comment.');
                    res.redirect('/campgrounds/' + found_campground._id);
                }
            });
        }
    });
});

// EDIT
router.get('/:comment_id/edit', middleware.check_comment_ownership, function(req, res){
    Comment.findById(req.params.comment_id, function(err, found_comment){
        if (err || !found_comment) {
            console.log(err);
            req.flash('error', 'That comment does not exist.');
            res.redirect('/campgrounds/' + req.params.id);
        } else {
            res.render('comments/edit', {campground_id: req.params.id, comment: found_comment});
        }
    });
});

// UPDATE
router.put('/:comment_id', middleware.check_comment_ownership, function(req, res){
    req.body.comment.time = moment(); // updating time to reflect most recent edit date
    Comment.findByIdAndUpdate(req.params.comment_id, req.body.comment, function(err, updated_comment){
        if(err){
            res.redirect('back');
        } else{
            req.flash('success', 'Updated comment.');
            res.redirect('/campgrounds/' + req.params.id);
        }
    });
});

// DESTROY
router.delete('/:comment_id', middleware.check_comment_ownership, function(req, res){
    Comment.findByIdAndRemove(req.params.comment_id, function(err){
        if(err){
            req.flash('error', 'Something went wrong.');
            res.redirect('back');
        } else{
            req.flash('success', 'Deleted comment.');
            res.redirect('back');
        }
    })
});

module.exports = router;
