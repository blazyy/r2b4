// IMPORTS
const express = require('express'),
    app = express(),
    mongoose = require('mongoose'),
    passport = require('passport'),
    bodyParser = require('body-parser'),
    User = require('./models/user'),
    LocalStrategy = require('passport-local'),
    passportLocalMongoose = require('passport-local-mongoose');

// SETUP
app.use(require('express-session')({
    secret: 'Cattus Maximillian',
    resave: false,
    saveUninitialized: false
}));
app.set('view engine', 'ejs');
app.use(bodyParser.urlencoded({extended: true}));
app.use(passport.initialize());
app.use(passport.session());

passport.use(new LocalStrategy(User.authenticate()));
passport.serializeUser(User.serializeUser());
passport.deserializeUser(User.deserializeUser());

mongoose.connect('mongodb://localhost:27017/auth_demo', {
        useNewUrlParser: true,
        useUnifiedTopology: true
    })
    .then(() => console.log('Connected to DB!'))
    .catch(error => console.log(error.message));

// ROUTES
app.get('/', function(req, res){
    res.render('home');
});

// isLoggedIn is the middleware, if the user is still logged in the current session,
// it executes next() which means the callback function will then execute
app.get('/secret', isLoggedIn, function(req, res){
    res.render('secret');
});

app.get('/register', function(req, res){
    res.render('register');
});

app.post('/register', function(req, res){
    User.register(new User({username:  req.body.username}), req.body.password, function(err, user){
        if(err){
            console.log(err);
            res.render('register');
        } else{
            // local strategy i.e. details stored locally
            passport.authenticate('local')(req, res, function(){
                res.redirect('/secret');
            });
        }
    });
});

app.get('/login', function(req, res){
    res.render('login');
});

app.get('/logout', function(req, res){
    req.logout();
    res.redirect('/');
});

app.post('/login', passport.authenticate('local', {
    successRedirect: '/secret',
    failureRedirect: '/login'
}));
// middleware function
function isLoggedIn(req, res, next){
    if(req.isAuthenticated()){
        return next();
    }
    res.redirect('/login');
}

app.listen(3000, function(){
    console.log("Server listening on port 3000...");
})
