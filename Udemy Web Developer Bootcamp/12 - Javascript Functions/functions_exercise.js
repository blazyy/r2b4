function isEven(num){
    return num % 2 === 0;
}

function factorial(num){
    let fact = 1;
    while(num > 1)
        fact *= num--;
    return fact;
}

function kebab_to_snake(expr){
    return expr.replace(/-/g, '_');
}
