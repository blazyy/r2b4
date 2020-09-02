console.log("Numbers between -10 and 19");
let num = -10;
while(num <= 19){
    console.log(num);
    num++;
}

console.log("Even numbers between 10 and 49");
num = 10;
while(num <= 40){
    if(num % 2 === 0)
        console.log(num);
    num++;
}

console.log("Odd numbers between 300 and 333");
num = 300;
while(num <= 333){
    if(num % 2 !== 0)
        console.log(num);
    num++;
}

console.log("All numbers divisible by 5 and 3 between 5 and 50");
num = 5;
while(num <= 50){
    if(num % 3 === 0 && num % 5 === 0)
        console.log(num);
    num++;
}
