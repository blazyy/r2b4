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


// Checking for any change in the number input
winning_score_input.addEventListener("change", function(){
    winning_score = Number(winning_score_input.value);
    if(winning_score < 0){
        msg_box.innerHTML = "Winning score cannot be negative!";
        game_over = true;
    }
    else{
        msg_box.innerHTML = "Playing to <span id=\"winning_score_display\">" + winning_score + "</span>";
        game_over = false;
    }
});

function reset(){
    winning_score_input.disabled = false;
    p1_score = 0;
    p2_score = 0;
    winning_score = 5;
    winning_score_input.value = winning_score;
    p1_score_display.textContent = p1_score;
    p2_score_display.textContent = p2_score;
    p1_score_display.classList.remove("green");
    p2_score_display.classList.remove("green");
    msg_box.innerHTML = "Playing to <span id=\"winning_score_display\">" + winning_score + "</span>";
    game_over = false;
}

// Resetting after game over
reset_button.addEventListener("click", reset);

// Player 1 button functionality
p1_button.addEventListener("click", function(){
    if(!game_over){
        p1_score++;
        p1_score_display.textContent = p1_score;
        winning_score_input.disabled = true;
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
        winning_score_input.disabled = true;
        p2_score++;
        p2_score_display.textContent = p2_score;
        if(p2_score === winning_score){
            p2_score_display.classList.add("green");
            msg_box.textContent = "Player 2 wins!"
            game_over = true;
        }
    }
});
