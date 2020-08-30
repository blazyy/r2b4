const express = require("express"),
    app = express(),
    body_parser = require("body-parser"),
    mongoose = require('mongoose'),
    comment_model = require('./models/comment'),
    campground_model = require('./models/campground'),
    seedDB = require('./seeds');

mongoose.connect('mongodb://localhost:27017/space_camp', {
        useNewUrlParser: true,
        useUnifiedTopology: true
    })
    .then(() => console.log('Connected to DB!'))
    .catch(error => console.log(error.message));

app.use(body_parser.urlencoded({extended: true}));
app.set("view engine", "ejs");
seedDB();

app.get("/", function(req, res) {
    res.render("landing");
});

// INDEX
app.get("/campgrounds", function(req, res) {
    campground_model.find({}, function(err, campgrounds_from_database) {
        if (err) {
            console.log(error);
        } else {
            res.render("campgrounds/index", {
                campgrounds: campgrounds_from_database
            });
        }
    });
});

// NEW - campground
app.get("/campgrounds/new", function(req, res) {
    res.render("campgrounds/new");
});

// CREATE - campground
app.post("/campgrounds", function(req, res) {
    let new_campground = {
        name: req.body.camp_name,
        image: req.body.camp_img_url,
        description: req.body.camp_description
    };
    campground_model.create(new_campground, function(err, new_campground) {
        if (err) {
            console.log(err);
        } else {
            res.redirect("/campgrounds");
        }
    });
});

// SHOW
app.get("/campgrounds/:id", function(req, res) {
    // The .populate("comments").exec() here just replaces the comment references with the actual content
    // of the comments themselves so that these can be sent as an object to the /show.js page
    campground_model.findById(req.params.id).populate("comments").exec(function(err, found_campground) {
        if (err) {
            console.log(err);
        } else {
            res.render("campgrounds/show", {
                campground: found_campground
            });
        }
    });
});

// NEW - comment
app.get("/campgrounds/:id/comments/new", function(req, res){
    campground_model.findById(req.params.id, function(err, found_campground){
        if(err){
            console.log(err);
        }
        else{
            res.render("comments/new", {campground: found_campground});
        }
    });
});

app.post("/campgrounds/:id/comments", function(req, res){
    campground_model.findById(req.params.id, function(err, found_campground){
        if(err){
            console.log(err);
        } else{
            comment_model.create(req.body.comment, function(err, new_comment){
                if(err){
                    console.log(err);
                } else{
                    found_campground.comments.push(new_comment);
                    found_campground.save();
                    res.redirect("/campgrounds/" + found_campground._id);
                }
            });
        }
    });
});

// CREATE - comment
app.get("*", function(req, res) {
    res.send("It seems you are lost! 🥱 <br> <a href='/'>Go Back</a>");
});

app.listen(3000, function(req, res) {
    console.log("Server listening on port 3000...");
});
