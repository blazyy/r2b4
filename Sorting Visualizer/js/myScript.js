var margin_top_percentage = 0.2;
var num_bars = 200;
var bar_color = 255;
var bar_width;
var bar_heights = [];
var currently_sorting = false;
var stopped = false;
var selected_sort = '1';
available_sorts = {
    '1': bubble_sort,
    '2': selection_sort
}

$(document).ready(function() {
    $('#start-button').on('click', function(){
        $('#start-button').attr('disabled', true);
        $('#reset-button').attr('disabled', true);
        $('#num-bars-range').attr('disabled', true);
        available_sorts[selected_sort]();
    });

    $('#reset-button').on('click', function(){
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
        selected_sort = $(this).val();
    })
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
                let temp = bar_heights[j];
                bar_heights[j] = bar_heights[j + 1];
                bar_heights[j + 1] = temp;
            }
        }
    }
    $('#reset-button').removeAttr('disabled');
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
        let temp = bar_heights[i];
        bar_heights[i] = bar_heights[min_idx];
        bar_heights[min_idx] = temp;
    }
    $('#reset-button').removeAttr('disabled');
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
