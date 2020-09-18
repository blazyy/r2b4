var margin_top_percentage = 0.2;
var num_bars = 200;
var bar_color = 255;
var bar_width;
var bar_heights = [];
var initial_resize = true;
var currently_sorting = false;
var stopped = false;

$(document).ready(function() {
    $('#start-button').on('click', function(){
        $('#start-button').attr('disabled', true);
        $('#reset-button').attr('disabled', true);
        bubble_sort();
    });

    $('#reset-button').on('click', function(){
        $('#start-button').removeAttr('disabled');
        generate_heights();
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
        bar_heights.push(Math.floor(Math.random() * ((windowHeight) - (windowHeight * margin_top_percentage))) + 30);
    }
}

function draw_bars() {
    width_pen = 0;
    for (var i = 0; i < num_bars; i++) {
        stroke(bar_color);
        fill(bar_color);
        rect(width_pen, height - bar_heights[i], bar_width, bar_heights[i]);
        width_pen += bar_width;
    }
}

async function bubble_sort() {
    currently_sorting = true;
    for (var i = 0; i < num_bars; i++) {
        for (var j = 0; j < num_bars - i - 1; j++) {
            if (bar_heights[j] > bar_heights[j + 1]) {
                await sleep(4); // 4 ms is the smallest delay possible using setTimeout()
                var temp = bar_heights[j];
                bar_heights[j] = bar_heights[j + 1];
                bar_heights[j + 1] = temp;
            }
        }
        // await sleep(1);
    }
    $('#reset-button').removeAttr('disabled');
    currently_sorting = false;
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
