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

const campground_routes = require('./routes/campgrounds'),
    comment_routes = require('./routes/comments'),
    index_routes = require('./routes/index');

mongoose.connect('mongodb://localhost:27017/space_camp', {
        useNewUrlParser: true,
        useUnifiedTopology: true
    })
    .then(() => console.log('Connected to DB!'))
    .catch(error => console.log(error.message));

app.use(body_parser.urlencoded({extended: true}));
app.set('view engine', 'ejs');
//seedDB();

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


// Note to self: changing the order of the 3 lines below messed things
// up. Idk why.
app.use('/campgrounds', campground_routes); // can remove "/campgrounds" prefix in campground routes if specified here.
app.use('/campgrounds/:id/comments', comment_routes); // same
app.use(index_routes);

app.listen(3000, function(req, res) {
    console.log('Server listening on port 3000...');
});
