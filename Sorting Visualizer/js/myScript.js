var margin_top_percentage = 0.2;
var num_bars = 200;
var bar_color = '#ffffff';
var bar_width;
var bar_heights = [];
var initial_resize = true;

$(document).ready(function() {
    const sort_button = document.getElementById('sort-button');
    // const reset_button = document.getElementById('reset-button');
    sort_button.addEventListener('click', function(){
        if(!isLooping()){
            loop();
        }
        bubble_sort();
    });
    // reset_button.addEventListener('click', function(){
    //     noLoop();
    //     generate_heights();
    //     resizeCanvas(windowWidth, windowHeight);
    // });
});

function setup() {
    createCanvas(windowWidth, windowHeight);
    bar_width = windowWidth / num_bars;
    generate_heights();
}

// draw() by default loops forever
function draw() {
    background(0);
    draw_bars();
    // noLoop();
}

function generate_heights() {
    bar_heights = [];
    for (var i = 0; i < num_bars; i++) {
        bar_heights.push(Math.floor(Math.random() * ((windowHeight) - (windowHeight * margin_top_percentage)) + 1));
    }
}

function draw_bars() {
    width_pen = 0;
    for (var i = 0; i < num_bars; i++) {
        noStroke();
        fill(255);
        rect(width_pen, 0, bar_width, bar_heights[i]);
        width_pen += bar_width;
    }
}

async function bubble_sort() {
    for (var i = 0; i < num_bars; i++) {
        for (var j = 0; j < num_bars - i - 1; j++) {
            if (bar_heights[j] > bar_heights[j + 1]) {
                await sleep(1);
                var temp = bar_heights[j];
                bar_heights[j] = bar_heights[j + 1];
                bar_heights[j + 1] = temp;
            }
        }
    }
}

function windowResized() {
    bar_width = windowWidth / num_bars;
    generate_heights();
    resizeCanvas(windowWidth, windowHeight);
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}
