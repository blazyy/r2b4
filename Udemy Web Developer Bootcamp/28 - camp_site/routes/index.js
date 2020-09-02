const express = require('express'),
    router = express.Router(),
    passport = require('passport'),
    User = require('../models/user')
async = require('async'),
    nodemailer = require('nodemailer'),
    crypto = require('crypto');

router.get('/', function(req, res) {
    res.render('landing');
});

// Register
router.get('/register', function(req, res) {
    res.render('register');
});

router.post('/register', function(req, res) {
    let new_user = new User({
        username: req.body.username,
        email: req.body.email
    });
    User.register(new_user, req.body.password, function(err, new_user) {
        if (err) {
            req.flash('error', err.message + "!");
            res.redirect('/register');
        } else {
            passport.authenticate('local')(req, res, function() {
                req.flash('success', 'Welcome to SpaceCamp, ' + new_user.username + "!");
                res.redirect('/campgrounds');
            });
        }
    });
});

router.get('/login', function(req, res) {
    res.render('login');
});

// passport.authenticate() is the middleware
router.post('/login', passport.authenticate('local', {
    successRedirect: '/campgrounds',
    failureRedirect: '/login'
}));

router.get('/logout', function(req, res) {
    req.logout();
    res.redirect('/campgrounds');
});

// Forgot Password
router.get('/forgot', function(req, res) {
    res.render('forgot');
});

// router.post('/forgot', function(req, res) {
//     let transporter = nodemailer.createTransport(options[, defaults]);
//     transporter.verify(function(error, success) {
//         if (error) {
//             console.log(error);
//         } else {
//             console.log("Server is ready to take our messages");
//         }
//     });
// req.flash('success', 'A password reset link will be sent to ' + req.body.email + '. If it exists.');
// res.redirect('/campgrounds');
// });

router.post('/forgot', function(req, res, next) {
    async.waterfall([
        function(done) {
            crypto.randomBytes(20, function(err, buf) {
                var token = buf.toString('hex');
                done(err, token);
            });
        },
        function(token, done) {
            User.findOne({
                email: req.body.email
            }, function(err, user) {
                if (!user) {
                    req.flash('success', 'A password reset link will be sent to ' + req.body.email + '. If it exists. (Check your spam folder!)');
                    res.redirect('/campgrounds');
                }
                user.reset_pw_token = token;
                user.reset_pw_token_expires_on = Date.now() + 3600000; // 1 hour
                user.save(function(err) {
                    done(err, token, user);
                });
            });
        },
        function(token, user, done) {
            var smtpTransport = nodemailer.createTransport({
                service: 'Gmail',
                auth: {
                    user: 'campsitefaaez@gmail.com',
                    pass: 'campsite123!'
                }
            });
            var mailOptions = {
                to: user.email,
                from: 'campsitefaaez@gmail.com',
                subject: 'CampSite™ Password Reset',
                text: 'You are receiving this because you (or someone else) have requested the reset of the password for your account.\n\n' +
                    'Please click on the following link to reset your password:\n\n' +
                    'http://' + req.headers.host + '/reset/' + token + '\n\n' +
                    'If you did not request this, please ignore this email and your password will remain unchanged.\n'
            };
            smtpTransport.sendMail(mailOptions, function(err) {
                if (err) {
                    console.log(err);
                } else {
                    req.flash('success', 'A password reset link will be sent to ' + req.body.email + '. If it exists.');
                    res.redirect('/campgrounds');
                }
            });
        }
    ], function(err) {
        if (err) return next(err);
        res.redirect('/forgot');
    });
});

router.get('/reset/:token', function(req, res) {
    User.findOne({
        reset_pw_token: req.params.token,
        reset_pw_token_expires_on: {
            $gt: Date.now()
        }
    }, function(err, user) {
        if (!user) {
            req.flash('error', 'Password reset token is invalid or has expired.');
            return res.redirect('/forgot');
        }
        res.render('reset', {
            token: req.params.token
        });
    });
});

router.post('/reset/:token', function(req, res) {
    async.waterfall([
        function(done) {
            User.findOne({
                reset_pw_token: req.params.token,
                reset_pw_token_expires_on: {
                    $gt: Date.now()
                }
            }, function(err, user) {
                if (!user) {
                    req.flash('error', 'Password reset token is invalid or has expired.');
                    return res.redirect('back');
                }
                if (req.body.password === req.body.confirm) {
                    user.setPassword(req.body.password, function(err) {
                        user.reset_pw_token = undefined;
                        user.reset_pw_token_expires_on = undefined;
                        user.save(function(err) {
                            req.logIn(user, function(err) {
                                done(err, user);
                            });
                        });
                    })
                } else {
                    req.flash("error", "Passwords do not match.");
                    return res.redirect('back');
                }
            });
        },
        function(user, done) {
            var smtpTransport = nodemailer.createTransport({
                service: 'Gmail',
                auth: {
                    user: 'learntocodeinfo@gmail.com',
                    pass: process.env.GMAILPW
                }
            });
            var mailOptions = {
                to: user.email,
                from: 'learntocodeinfo@mail.com',
                subject: 'Your password has been changed',
                text: 'Hello,\n\n' +
                    'This is a confirmation that the password for your account ' + user.email + ' has just been changed.\n'
            };
            smtpTransport.sendMail(mailOptions, function(err) {
                req.flash('success', 'Success! Your password has been changed.');
                done(err);
            });
        }
    ], function(err) {
        res.redirect('/campgrounds');
    });
});
// CREATE - comment
router.get('*', function(req, res) {
    res.sendStatus(404);
});

module.exports = router;
