var margin_top_percentage = 0.3;
var num_bars = 200;
var bar_color = 255;
var bar_width;
var bar_heights = [];
var currently_sorting = false;
var stopped = false;
var selected_sort = '1';
available_sorts = {
    '1': bubble_sort,
    '2': selection_sort,
    '3': quick_sort,
    '4': insertion_sort
}

$(document).ready(function() {
    $('#start-button').on('click', function(){
        $('#start-button').attr('disabled', true);
        $('#new-button').attr('disabled', true);
        $('#num-bars-range').attr('disabled', true);
        $('#reset-button').removeAttr('disabled');
        available_sorts[selected_sort]();
    });

    $('#new-button').on('click', function(){
        generate_heights();
        $('#start-button').removeAttr('disabled');
    })

    $('#num-bars-range').on('input', function(){
        $('#start-button').removeAttr('disabled');
        num_bars = $(this).val();
        bar_width = windowWidth / num_bars;
        generate_heights();
    });

    $('#sort-select-dropdown').on('change', function(){
        $('#start-button').removeAttr('disabled');
        selected_sort = $(this).val();
    })

    $('#reset-button').on('click', function(){
        window.location.reload();
    });
});

function setup() {
    frameRate(60);
    createCanvas(windowWidth, windowHeight);
    bar_width = windowWidth / num_bars;
    generate_heights();
}

function draw() {
    background(0);
    draw_bars();
}

function generate_heights() {
    bar_heights = [];
    for (var i = 0; i < num_bars; i++) {
        // The 24.375 is just a ratio I calculated which increases the height of the bars so that the bars don't have a height that seems empty
        bar_heights.push(Math.floor(Math.random() * ((windowHeight) - (windowHeight * margin_top_percentage))) + (windowHeight/24.375));
    }
}

function draw_bars() {
    for (var i = 0; i < num_bars; i++) {
        stroke(bar_color);
        fill(bar_color);
        rect(i * bar_width, height - bar_heights[i], bar_width, bar_heights[i]);
    }
}

async function bubble_sort() {
    for (var i = 0; i < num_bars; i++) {
        for (var j = 0; j < num_bars - i - 1; j++) {
            if (bar_heights[j] > bar_heights[j + 1]) {
                await sleep(4); // 4 ms is the smallest delay possible using setTimeout()
                swap(j, j+1);
            }
        }
    }
    $('#new-button').removeAttr('disabled');
    $('#num-bars-range').removeAttr('disabled');
}

async function selection_sort(){
    for(var i = 0; i < num_bars; i++){
        var min_idx = i;
        for(var j = i; j < num_bars; j++){
            if(bar_heights[j] < bar_heights[min_idx]){
                min_idx = j;
            }
        }
        await sleep(4);
        swap(i, min_idx);
    }
    $('#new-button').removeAttr('disabled');
    $('#num-bars-range').removeAttr('disabled');
}

async function partition(start, end){
    var pivot = bar_heights[end];
    var partn_idx = start;
    for(var i = start; i < end; i++){
        if(bar_heights[i] <= pivot){
            await sleep(4);
            await swap(i, partn_idx)
            partn_idx++;
        }
    }
    await swap(partn_idx, end);
    return partn_idx;
}

async function quick_sort(start = 0, end = num_bars-1){
    if(start < end){
        var partn_idx = await partition(start, end);
        await Promise.all([
            quick_sort(start, partn_idx - 1),
            quick_sort(partn_idx + 1, end)
        ]);
    } else{
        $('#new-button').removeAttr('disabled');
        $('#num-bars-range').removeAttr('disabled');
    }
}

async function insertion_sort(){
    for(var i = 1; i < num_bars; i++){
        var current = i;
        var value = bar_heights[i];
        while(current > 0 && bar_heights[current - 1] > value){
            bar_heights[current] = bar_heights[current - 1];
            current--;
        }
        await sleep(4);
        bar_heights[current] = value;
    }
    $('#new-button').removeAttr('disabled');
    $('#num-bars-range').removeAttr('disabled');
}

function windowResized() {
    if(!currently_sorting){
        bar_width = windowWidth / num_bars;
        generate_heights();
        resizeCanvas(windowWidth, windowHeight);
    }
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

function swap(x, y){
    var temp = bar_heights[x];
    bar_heights[x] = bar_heights[y];
    bar_heights[y] = temp;
}
