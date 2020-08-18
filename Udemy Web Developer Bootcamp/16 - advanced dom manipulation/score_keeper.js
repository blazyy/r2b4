let p1_score = 0;
let p2_score = 0;
let game_over = false;
let winning_score = 5;
const p1_score_display = document.querySelector("#p1_score_display");
const p2_score_display = document.querySelector("#p2_score_display");
const p1_button = document.querySelector("#p1_button");
const p2_button = document.querySelector("#p2_button");
const reset_button = document.querySelector("#reset_button");
const winning_score_input = document.querySelector("#winning_score_input");
const winning_score_display = document.querySelector("#winning_score_display");
const msg_box = document.querySelector("#msg_box");


// Checking for any change he number input
winning_score_input.addEventListener("change", function(){
    winning_score = Number(winning_score_input.value);
    winning_score_display.textContent = winning_score;
});

// Player 1 button functionality
p1_button.addEventListener("click", function(){
    if(!game_over){
        p1_score++;
        p1_score_display.textContent = p1_score;
        if(p1_score === winning_score){
            p1_score_display.classList.add("green");
            msg_box.textContent = "Player 1 wins!"
            game_over = true;
        }
    }
});

// Player 2 button functionality
p2_button.addEventListener("click", function(){
    if(!game_over){
        p2_score++;
        p2_score_display.textContent = p2_score;
        if(p2_score === winning_score){
            p2_score_display.classList.add("green");
            msg_box.textContent = "Player 2 wins!"
            game_over = true;
        }
    }
});

// Resetting after game over
reset_button.addEventListener("click", function(){
    p1_score = 0;
    p2_score = 0;
    p1_score_display.textContent = p1_score;
    p2_score_display.textContent = p2_score;
    p1_score_display.classList.remove("green");
    p2_score_display.classList.remove("green");
    msg_box.innerHTML = "Playing to <span id=\"winning_score_display\">" + winning_score + "</span>";
    game_over = false;
});
