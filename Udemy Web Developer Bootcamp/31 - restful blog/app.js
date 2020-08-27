const express = require('express'),
    app = express(),
    body_parser = require('body-parser'),
    mongoose = require('mongoose'),
    method_override = require('method-override'),
    express_sanitizer = require('express-sanitizer');

mongoose.connect('mongodb://localhost:27017/restful_blog_app', {
        useNewUrlParser: true,
        useUnifiedTopology: true
    })
    .then(() => console.log('Connected to DB!'))
    .catch(error => console.log(error.message));

const blog_schema = new mongoose.Schema({
    title: String,
    image: String,
    body: String,
    created_at: {
        type: Date,
        default: Date.now
    }
});

const blog_model = mongoose.model("blog", blog_schema);

app.set("view engine", "ejs");
app.use(express.static("public"));
app.use(body_parser.urlencoded({
    extended: true
}));
app.use(express_sanitizer());
app.use(method_override("_method"));

// INDEX
app.get("/blogs", function(req, res) {
    blog_model.find({}, function(err, blogs_from_db) {
        if (err) {
            console.log(err);
        } else {
            res.render("index", {
                blogs: blogs_from_db
            });
        }
    });
});

// NEW
app.get("/blogs/new", function(req, res) {
    res.render("new");
});

// CREATE
app.post("/blogs", function(req, res) {
    req.body.blog.body = req.sanitize(req.body.blog.body);
    blog_model.create(req.body.blog, function(err, new_blog) {
        if (err) {
            console.log(err);
        } else {
            res.redirect("/blogs");
        }
    });
});

// SHOW
app.get("/blogs/:id", function(req, res) {
    blog_model.findById(req.params.id, function(err, found_blog) {
        if (err) {
            console.log(err);
        } else {
            res.render("show", {
                blog: found_blog
            });
        }
    });
});

// EDIT
app.get("/blogs/:id/edit", function(req, res) {
    blog_model.findById(req.params.id, function(err, found_blog) {
        if (err) {
            console.log(err);
        } else {
            res.render("edit", {
                blog: found_blog
            });
        }
    });
});

// UPDATE
app.put("/blogs/:id", function(req, res) {
    req.body.blog.body = req.sanitize(req.body.blog.body);
    blog_model.findByIdAndUpdate(req.params.id, req.body.blog, function(err, updated_blog) {
        if (err) {
            console.log(err);
        } else {
            res.redirect("/blogs/" + req.params.id);
        }
    });
});

// DELETE
app.delete("/blogs/:id", function(req, res) {
    blog_model.findByIdAndRemove(req.params.id, function(err) {
        if (err) {
            console.log(err);
        } else {
            res.redirect("/blogs");
        }
    });
});

app.listen(3000, function(req, res) {
    console.log("Server listening on port 3000...");
});
