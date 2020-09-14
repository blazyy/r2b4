const express = require('express'),
    router = express.Router({mergeParams: true}), // to enable the req object to be read, if this option isn't specified then no objects will be passed
    Campground = require('../models/campground'),
    Review = require('../models/review'),
    middleware = require('../middleware'),
    moment = require('moment');

// NEW - review
router.get('/new', middleware.is_logged_in, function(req, res){
    Campground.findById(req.params.id).populate('reviews').exec(function(err, found_campground){
        if (err || !found_campground) {
            console.log(err);
            req.flash('error', 'That campground does not exist.');
            res.redirect('/campgrounds');
        } else {
            let review_already_exists = false;
            found_campground.reviews.forEach(function(review){
                if(req.user._id.equals(review.author.id) && !req.user.is_admin && !review_already_exists){
                    review_already_exists = true;
                    req.flash('error', 'You can only post one review!');
                    res.redirect('/campgrounds/' + found_campground._id);
                }
            });
            if(!review_already_exists){
                res.render('reviews/new', {campground: found_campground});
            }
        }
    });
});

// CREATE - review
router.post('/', middleware.is_logged_in, function(req, res){
    Campground.findById(req.params.id).populate('reviews').exec(function(err, found_campground){
        if(err){
            req.flash('error', 'That campground does not exist.');
            res.redirect('/campgrounds');
        } else{
            Review.create(req.body.review, function(err, new_review){
                if(err){
                    req.flash('error', 'That review does not exist.');
                    res.redirect('/campgrounds/' + found_campground._id);
                } else{
                    User.update({_id: req.user._id}, {$inc: {'reviews_given': 1}}, function(err, updated_campground){
                        if(err){
                            console.log(err);
                        } else{
                            new_review.author.id = req.user._id; // req.user from PassportJS? I think so.
                            new_review.author.username = req.user.username;
                            new_review.save();
                            found_campground.reviews.push(new_review);
                            found_campground.avg_rating = calculate_avg_rating(found_campground.reviews);
                            found_campground.save();
                            req.flash('success', 'Added new review.');
                            res.redirect('/campgrounds/' + found_campground._id);
                        }
                    });
                }
            });
        }
    });
});

// EDIT
router.get('/:review_id/edit', middleware.check_review_ownership, function(req, res){
    Review.findById(req.params.review_id, function(err, found_review){
        if (err || !found_review) {
            console.log(err);
            req.flash('error', 'That review does not exist.');
            res.redirect('/campgrounds/' + req.params.id);
        } else {
            res.render('reviews/edit', {campground_id: req.params.id, review: found_review});
        }
    });
});

// UPDATE
router.put('/:review_id', middleware.check_review_ownership, function(req, res){
    req.body.review.time = moment(); // updating time to reflect most recent edit date
    Review.findByIdAndUpdate(req.params.review_id, req.body.review, function(err, updated_review){
        if(err){
            res.redirect('back');
        } else{
            Campground.findById(req.params.id).populate('reviews').exec(function(err, found_campground){
                if(err){
                    req.flash('error', 'That campground does not exist.');
                    res.redirect('/campgrounds');
                } else{
                    found_campground.avg_rating = calculate_avg_rating(found_campground.reviews);
                    found_campground.save();
                    req.flash('success', 'Updated review.');
                    res.redirect('/campgrounds/' + req.params.id);
                }
            });
        }
    });
});

// DESTROY
router.delete('/:review_id', middleware.check_review_ownership, function(req, res){
    Review.findByIdAndRemove(req.params.review_id, function(err){
        if(err){
            req.flash('error', 'Something went wrong.');
            res.redirect('back');
        } else{
            Campground.findById(req.params.id).populate('reviews').exec(function(err, found_campground){
                if(err){
                    req.flash('error', 'That campground does not exist.');
                    res.redirect('/campgrounds');
                } else{
                    User.update({_id: req.user._id}, {$inc: {'reviews_given': -1}}, function(err, updated_campground){
                        if(err){
                            console.log(err);
                        } else{
                            found_campground.avg_rating = calculate_avg_rating(found_campground.reviews);
                            found_campground.save();
                            req.flash('success', 'Deleted review.');
                            res.redirect('back');
                        }
                    });
                }
            });

        }
    })
});

function calculate_avg_rating(reviews){
    if(reviews.length === 0){
        return 0;
    }
    let avg = 0;
    reviews.forEach(function(review){
        avg += review.rating;
    });
    return avg/reviews.length;
}

module.exports = router;
