const movies = [
    {
        "name": "Interstellar",
        "rating":  9.5,
        "has_watched": true
    },
    {
        "name": "Pulp Fiction",
        "rating": 10,
        "has_watched": false
    },
    {
        "name": "Arrival",
        "rating": 8.5,
        "has_watched": false
    },
    {
        "name": "Inception",
        "rating": 10,
        "has_watched": true
    }
]

movies.forEach(function(movie){
    if(movie.has_watched)
        console.log("You have seen \"" + movie.name + "\" - " + movie.rating + " stars");
    else
        console.log("You have not seen \"" + movie.name + "\" - " + movie.rating + " stars");
})
