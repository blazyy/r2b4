const mongoose = require('mongoose');

const campground_schema = new mongoose.Schema({
    name: String,
    image: String,
    description: String,
    price: Number,
    location: String,
    author: {
        id: {
            type: mongoose.Schema.Types.ObjectId,
            ref: 'user'
        },
        username: String
    },
    reviews: [
        {
            type: mongoose.Schema.Types.ObjectId,
            ref: 'review'
        }
    ],
    avg_rating: Number,
    time: {
        type: Date,
        default: Date.now
    }
});

module.exports = mongoose.model("campground", campground_schema);
