const express = require('express'),
    router = express.Router({mergeParams: true}), // to enable the req object to be read, if this option isn't specified then no objects will be passed
    Campground = require('../models/campground'),
    Comment = require('../models/comment');

// NEW - comment
router.get('/new', isLoggedIn, function(req, res){
    Campground.findById(req.params.id, function(err, found_campground){
        if(err){
            console.log(err);
        }
        else{
            res.render('comments/new', {campground: found_campground});
        }
    });
});

// CREATE - comment
router.post('/', isLoggedIn, function(req, res){
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
                    res.redirect('/campgrounds/' + found_campground._id);
                }
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
