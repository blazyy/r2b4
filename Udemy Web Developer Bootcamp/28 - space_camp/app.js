const express = require('express'),
    app = express(),
    body_parser = require('body-parser'),
    mongoose = require('mongoose'),
    flash = require('connect-flash'),
    passport = require('passport'),
    local_strategy = require('passport-local'),
    method_override = require('method-override');
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
passport.use(new local_strategy(User.authenticate()));
passport.serializeUser(User.serializeUser());
passport.deserializeUser(User.deserializeUser());
app.use(method_override('_method'));
app.use(flash());

// The function below is a middleware that passes the current_user (if logged in)
// to every .ejs template. We don't have to manually send it in the object in the
// render function for all routes.  his is needed since the navbar exists on all pages,
// and the navbar needs to know if a user is logged in or not to display or
// hide any respective options

// Passes current_user and flash messages to every single template,
// this way we don't have to send as an object to each template individually.
app.use(function(req, res, next){
    res.locals.current_user = req.user; // req.user is from PassportJS
    res.locals.error = req.flash('error'); // the 'error' is merely a key for connect-flash alerts. not plaintext
    res.locals.success = req.flash('success'); // same here
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
