function print_reverse(arr){
    for(let i = arr.length; i >= 0; i--)
        console.log(arr[i]);
}

function is_uniform(arr){
    const first_ele = arr[0];
    for(let i = 1; i < arr.length; i++)
        if(arr[i] !== first_ele)
            return false;
    return true;
}

function sum_array(arr){
    let sum = 0;
    for(let i = 0; i < arr.length; i++)
        sum += arr[i];
    return sum;
}

function max(arr){
    let max = arr[0];
    for(let i = 0; i < arr.length; i++)
        if(arr[i] > max)
            max = arr[i];
    return max;
}
