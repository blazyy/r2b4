var express = require("express");
var app = express();
var body_parser = require("body-parser");
const friends = ['Harry', 'Larry', 'Barry', 'Carrie', 'Mary'];


// app.use(express.static("public"));
app.use(body_parser.urlencoded({extended: true})); // needed to extract values from the req.body object in a POST request and store into a JS variable. without this it'll just be undefined.

app.set("view engine", "ejs");

app.get("/", function(req, res){
    res.send("Welcome to the homepage!");
});

app.get("/friends", function(req, res){
    res.render("friends", {friends: friends});
});

app.post("/addfriend", function(req, res){
    var new_friend = req.body.name;
    friends.push(new_friend);
    res.redirect("/friends");
});

app.listen(3000, function(){
    console.log("Server listening on port 3000!");
});
