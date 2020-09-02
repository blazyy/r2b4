const mongoose = require('mongoose');

const campground_schema = new mongoose.Schema({
    name: String,
    image: String,
    description: String,
    price: Number,
    author: {
        id: {
            type: mongoose.Schema.Types.ObjectId,
            ref: 'user'
        },
        username: String
    },
    comments: [
        {
            type: mongoose.Schema.Types.ObjectId,
            ref: "comment"
        }
    ],
    time: {
        type: Date,
        default: Date.now
    }
});

module.exports = mongoose.model("campground", campground_schema);
