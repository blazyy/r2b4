const mongoose = require('mongoose');

const comment_schema = mongoose.Schema({
    text: String,
    author: {
        id: {
            type: mongoose.Schema.Types.ObjectId,
            ref: 'user'
        },
        username: String
    },
    time: mongoose.Schema.Types.Date
})

module.exports = mongoose.model('comment', comment_schema);
