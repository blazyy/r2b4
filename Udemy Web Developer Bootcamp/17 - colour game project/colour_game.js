const squares = document.querySelectorAll(".square");
const picked_color_display = document.querySelector("#picked_color_display");
const msg_box = document.querySelector("#msg_box");
const new_colours_button = document.querySelector("#new_colours_button");
const header = document.querySelector("h1");
const easy_button = document.querySelector("#easy_button");
const hard_button = document.querySelector("#hard_button");
let number_of_squares = 9;
let picked_colour;


function fill_squares(){
    header.style.backgroundColor = "steelblue";
    msg_box.textContent = "";
    new_colours_button.textContent = "New Colours";
    let picked_colour_index = Math.floor(Math.random() * number_of_squares);
    for(let i = 0; i < number_of_squares; i++){
        let r = Math.floor(Math.random() * 256);
        let g = Math.floor(Math.random() * 256);
        let b = Math.floor(Math.random() * 256);
        let random_colour = "rgb(" + r + ", " + g + ", " + b + ")";
        if(i === picked_colour_index){
            picked_color_display.textContent = random_colour;
            picked_colour = random_colour;
        }
        squares[i].style.backgroundColor = random_colour;
    }
}

for(let i = 0; i < number_of_squares; i++){
    squares[i].addEventListener("click", function(){
        if(this.style.backgroundColor === picked_colour){
            new_colours_button.textContent = "Play Again?";
            msg_box.textContent = "Correct!";
            header.style.backgroundColor = picked_colour;
            for(let i = 0; i < number_of_squares; i++)
                squares[i].style.backgroundColor = picked_colour;
        }
        else{
            msg_box.textContent = "Try Again!";
            this.style.backgroundColor = "#232323";
        }
    });
}

new_colours_button.addEventListener("click", fill_squares);

easy_button.addEventListener("click", function(){
    hard_button.classList.remove("selected");
    easy_button.classList.add("selected");
    number_of_squares = 6;
    for(let i = 6; i < 9; i++){
        squares[i].style.display = "none";
    }
    fill_squares();
});

hard_button.addEventListener("click", function(){
    easy_button.classList.remove("selected");
    hard_button.classList.add("selected");
    for(let i = 6; i < 9; i++){
        squares[i].style.display = "block";
    }
    number_of_squares = 9;
    fill_squares()
});

fill_squares();
