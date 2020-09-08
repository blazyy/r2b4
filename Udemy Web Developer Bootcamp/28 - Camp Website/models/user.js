const mongoose = require('mongoose');
const passport_local_mongoose = require('passport-local-mongoose');

const user_schema = mongoose.Schema({
    username: {type: String, unique: true},
    display_picture: {type: String, default: 'https://www.clipartkey.com/mpngs/m/152-1520367_user-profile-default-image-png-clipart-png-download.png'},
    email: {type: String, unique: true},
    about: {type: String, default: ''},
    password: String,
    reset_pw_token: String,
    reset_pw_token_expires_on: Date,
    campgrounds_added: {type: Number, default: 0},
    reviews_given: {type: Number, default: 0}
});

user_schema.plugin(passport_local_mongoose);

module.exports = mongoose.model('user', user_schema);
