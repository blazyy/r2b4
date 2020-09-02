const mongoose = require('mongoose');
const passport_local_mongoose = require('passport-local-mongoose');

const user_schema = mongoose.Schema({
    username: {type: String, unique: true},
    email: {type: String, unique: true},
    password: String,
    reset_pw_token: String,
    reset_pw_token_expires_on: Date
});

user_schema.plugin(passport_local_mongoose);

module.exports = mongoose.model('user', user_schema);
