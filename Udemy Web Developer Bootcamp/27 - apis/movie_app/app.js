// https://www.omdbapi.com/?s=interstellar&apikey=2fc25eac
const express = require('express');
const axios = require('axios');
const body_parser = require("body-parser");
const app = express();
const API_KEY = '2fc25eac';

app.use(body_parser.urlencoded({
    extended: true
}));

app.set('view engine', 'ejs');

app.get("/", function(req, res) {
    res.render("home");
});

app.get("/search", function(req, res) {
    let query_url = 'https://www.omdbapi.com/?s=' + req.query.movie_name + '&apikey=' + API_KEY;
    axios.get(query_url)
        .then(function(response) {
            if(!response.data['Search']){
                res.send("No movies found with that name! 🙁 <br> <a href='/'>Go back</a>");
            }
            else{
                movies = response.data['Search'];
                res.render("movies", {
                    movies: movies
                });
            }
        })
        .catch(function(error) {
            console.log(error);
        });
});

app.get("*", function(req, res) {
    res.send("It seems you are lost! 🙁");
});

app.listen(3000, function() {
    console.log("Server listening on port 3000...");
});
