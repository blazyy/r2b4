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

app.post("/search", function(req, res) {
    let query_url = 'https://www.omdbapi.com/?s=' + req.body.movie_name + '&apikey=' + API_KEY;
    let movies = [];
    axios.get(query_url)
        .then(function(response) {
            if(!response.data['Search']){
                res.send("No movies found with that name! 🙁");
            }
            else{
                response.data['Search'].forEach(function(movie) {
                    movies.push(movie['Title']);
                });
            }
        })
        .catch(function(error) {
            console.log(error);
        })
        .then(function() {
            res.render("movies", {
                movies: movies
            });
        });
});

app.get("*", function(req, res) {
    res.send("It seems you are lost! 🙁");
});

app.listen(3000, function() {
    console.log("Server listening on port 3000...");
});
