const arr = [];
const arr_length = 10;

for(let i = 0; i < arr_length; i++)
    arr.push(Math.floor(Math.random() * 100));

const sum = arr.reduce(function(a, b){
    return a + b;
});

console.log("Generated Array: " + arr);
console.log("Average: " + sum/arr_length);
