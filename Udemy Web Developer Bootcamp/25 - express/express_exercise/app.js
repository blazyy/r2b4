const express = require("express");
const app = express();

app.get("/", function (req, res){
    res.send("Hey there, welcome to my assignment!");
});

app.get("/speak/pig", function(req, res){
    res.send("The pig says 'Oink!'");
});

app.get("/speak/cow", function(req, res){
    res.send("The cow says 'Moo!'");
});

app.get("/speak/dog", function(req, res){
    res.send("The dog says 'Woof Woof!'");
});

app.get("/repeat/:word/:times", function(req, res){
    let return_string = "";
    for(let i = 0; i < Number(req.params.times); i++)
        return_string += " " + req.params.word;
    res.send(return_string);
});

app.get("*", function(req, res){
    res.send("Sorry, page not found... what are you doing with your life?");
});

app.listen(3000, function(){
    console.log("Server listening on port 3000...");
});
