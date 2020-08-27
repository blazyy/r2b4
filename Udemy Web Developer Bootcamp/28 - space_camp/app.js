const express = require("express"),
    app = express(),
    body_parser = require("body-parser"),
    mongoose = require('mongoose');

mongoose.connect('mongodb://localhost:27017/space_camp', {
        useNewUrlParser: true,
        useUnifiedTopology: true
    })
    .then(() => console.log('Connected to DB!'))
    .catch(error => console.log(error.message));

const campground_schema = new mongoose.Schema({
    name: String,
    image: String,
    description: String
});

const campground_model = mongoose.model("campground", campground_schema);

app.use(body_parser.urlencoded({
    extended: true
}));

app.set("view engine", "ejs");

app.get("/", function(req, res) {
    res.render("landing");
});

app.get("/campgrounds", function(req, res) {
    campground_model.find({}, function(err, campgrounds_from_database) {
        if (err) {
            console.log(error);
        } else {
            res.render("index", {
                campgrounds: campgrounds_from_database
            });
        }
    });
});

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

app.get("/campgrounds/new", function(req, res) {
    res.render("new");
});

app.get("/campgrounds/:id", function(req, res) {
    campground_model.findById(req.params.id, function(err, found_campgroud) {
        if (err) {
            console.log(err);
        } else {
            res.render("show", {
                campground: found_campgroud
            });
        }
    });
});

app.get("*", function(req, res) {
    res.send("It seems you are lost! 🥱 <br> <a href='/'>Go Back</a>");
});

app.listen(3000, function(req, res) {
    console.log("Server listening on port 3000...");
});
