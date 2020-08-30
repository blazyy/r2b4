const express = require('express'),
    app = express(),
    body_parser = require('body-parser'),
    mongoose = require('mongoose'),
    passport = require('passport'),
    LocalStrategy = require('passport-local'),
    Comment = require('./models/comment'),
    Campground = require('./models/campground'),
    User = require('./models/user'),
    seedDB = require('./seeds');

mongoose.connect('mongodb://localhost:27017/space_camp', {
        useNewUrlParser: true,
        useUnifiedTopology: true
    })
    .then(() => console.log('Connected to DB!'))
    .catch(error => console.log(error.message));

app.use(body_parser.urlencoded({extended: true}));
app.set('view engine', 'ejs');
seedDB();

app.use(require('express-session')({
    secret: 'Cattus Maximillian',
    resave: false,
    saveUninitialized: false
}));
app.use(passport.initialize());
app.use(passport.session());
passport.use(new LocalStrategy(User.authenticate()));
passport.serializeUser(User.serializeUser());
passport.deserializeUser(User.deserializeUser());

// The function below is a middleware that passes the current_user (if logged in)
// to every .ejs template. We don't have to manually send it in the object in the
// render function for all routes.  his is needed since the navbar exists on all pages,
// and the navbar needs to know if a user is logged in or not to display or
// hide any respective options

app.use(function(req, res, next){
    res.locals.current_user = req.user; // req.user is from PassportJS
    next();
});

app.get('/', function(req, res) {
    res.render('landing');
});

// INDEX
app.get('/campgrounds', function(req, res) {
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
app.get('/campgrounds/new', function(req, res) {
    res.render('campgrounds/new');
});

// CREATE - campground
app.post('/campgrounds', function(req, res) {
    let new_campground = {
        name: req.body.camp_name,
        image: req.body.camp_img_url,
        description: req.body.camp_description
    };
    Campground.create(new_campground, function(err, new_campground) {
        if (err) {
            console.log(err);
        } else {
            res.redirect('/campgrounds');
        }
    });
});

// SHOW
app.get('/campgrounds/:id', function(req, res) {
    // The .populate('comments').exec() here just replaces the comment references with the actual content
    // of the comments themselves so that these can be sent as an object to the /show.js page
    Campground.findById(req.params.id).populate('comments').exec(function(err, found_campground) {
        if (err) {
            console.log(err);
        } else {
            res.render('campgrounds/show', {
                campground: found_campground
            });
        }
    });
});

// NEW - comment
app.get('/campgrounds/:id/comments/new', isLoggedIn, function(req, res){
    Campground.findById(req.params.id, function(err, found_campground){
        if(err){
            console.log(err);
        }
        else{
            res.render('comments/new', {campground: found_campground});
        }
    });
});

app.post('/campgrounds/:id/comments', isLoggedIn, function(req, res){
    Campground.findById(req.params.id, function(err, found_campground){
        if(err){
            console.log(err);
        } else{
            Comment.create(req.body.comment, function(err, new_comment){
                if(err){
                    console.log(err);
                } else{
                    found_campground.comments.push(new_comment);
                    found_campground.save();
                    res.redirect('/campgrounds/' + found_campground._id);
                }
            });
        }
    });
});

// Register
app.get('/register', function(req, res){
    res.render('register');
});

app.post('/register', function(req, res){
    let new_user = new User({username: req.body.username});
    User.register(new_user, req.body.password, function(err, new_user){
        if(err){
            console.log(err);
        }
        else{
            passport.authenticate('local')(req, res, function(){
                res.redirect('/campgrounds');
            });
        }
    });
});

app.get('/login', function(req, res){
    res.render('login');
});

// passport.authenticate() is the middleware
app.post('/login', passport.authenticate('local', {
    successRedirect: '/campgrounds',
    failureRedirect: '/login'
}));

app.get('/logout', function(req, res){
    req.logout();
    res.redirect('/campgrounds');
});

function isLoggedIn(req, res, next){
    if(req.isAuthenticated()){
        return next();
    }
    res.redirect('/login');
}

// CREATE - comment
app.get('*', function(req, res) {
    res.send('It seems you are lost! 🥱 <br> <a href='/'>Go Back</a>');
});

app.listen(3000, function(req, res) {
    console.log('Server listening on port 3000...');
});
