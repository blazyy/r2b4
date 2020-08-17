const age = Number(prompt("What is your age?"));

if(age < 0)
    console.log("Your age is negative!");
if(age == 21)
    console.log("Happy 21st birthday!");
if(age % 2 != 0)
    console.log("Your age is odd!");

const squared_age = Math.sqrt(age);
if(Math.ceil(squared_age) - squared_age === 0)
    console.log("Your age is a perfect square!");
