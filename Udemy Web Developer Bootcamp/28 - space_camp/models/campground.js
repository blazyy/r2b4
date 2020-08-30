const mongoose = require('mongoose');

const campground_schema = new mongoose.Schema({
    name: String,
    image: String,
    description: String,
    comments: [
        {
            type: mongoose.Schema.Types.ObjectId,
            ref: "comment"
        }
    ]
});

module.exports = mongoose.model("campground", campground_schema);
