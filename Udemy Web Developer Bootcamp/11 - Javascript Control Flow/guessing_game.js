const rand_num = Math.floor(Math.random() * 100) + 1;
var guessed_num;

guessed_num = Number(prompt("Guess a number between 1 to 100"));

if(guessed_num == rand_num)
    alert("Correct! You guessed on the first try!");
else{
    while(guessed_num != rand_num){
        if(guessed_num < rand_num)
            guessed_num = Number(prompt("Go higher!"));
        else if(guessed_num > rand_num)
            guessed_num = Number(prompt("Go lower!"));
    }
    alert("Correct!");
}
