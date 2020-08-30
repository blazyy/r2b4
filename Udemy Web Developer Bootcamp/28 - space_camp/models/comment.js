const mongoose = require('mongoose');

const comment_schema = mongoose.Schema({
    text: String,
    author: String
})

module.exports = mongoose.model("comment", comment_schema);
