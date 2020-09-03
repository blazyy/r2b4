const mongoose = require('mongoose');

const review_schema = mongoose.Schema({
    text: String,
    author: {
        id: {
            type: mongoose.Schema.Types.ObjectId,
            ref: 'user'
        },
        username: String
    },
    time: {
        type: Date,
        default: Date.now
    },
    rating: Number
})

module.exports = mongoose.model('review', review_schema);
