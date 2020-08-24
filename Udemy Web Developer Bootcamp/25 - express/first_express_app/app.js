const express = require("express");
const app = express();

app.get("/", function(req, res){
    res.send("Hey there!");
});

app.get("/bye", function(req, res){
    res.send("Goodbye :(");
});

app.get("/r/:subreddit_name", function(req, res){
    res.send("Omg, you're in the " + req.params.subreddit_name + " subreddit!");
});

app.get("*", function(req, res){
    res.send("It seems you are lost! :(");
});

app.listen(3000, function() {
  console.log('Server listening on port 3000');
});
