var margin_top_percentage = 0.3;
var num_bars = 200;
var bar_color = 255;
var bar_width;
var bar_heights = [];
var bar_colors = [];
var bar_color_width = 2;
var currently_sorting = false;
var stopped = false;
var selected_sort = 'bubble';
available_sorts = {
    'bubble': bubble_sort,
    'selection': selection_sort,
    'quicksort_l': quick_sort_lomuto,
    'insertion': insertion_sort,
    'merge': merge_sort
}

$(document).ready(function() {
    $('#start-button').on('click', function() {
        $('#start-button, #new-button, #num-bars-range').attr('disabled', true);
        $('#reset-button').removeAttr('disabled');
        available_sorts[selected_sort]();
    });

    $('#new-button').on('click', function() {
        generate_heights();
        $('#start-button').removeAttr('disabled');
    })

    $('#num-bars-range').on('input', function() {
        $('#start-button').removeAttr('disabled');
        num_bars = $(this).val();
        bar_width = windowWidth / num_bars;
        generate_heights();
    });

    $('#sort-select-dropdown').on('change', function() {
        $('#start-button').removeAttr('disabled');
        selected_sort = $(this).val();
    })

    $('#reset-button').on('click', function() {
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
        bar_heights.push(Math.floor(Math.random() * ((windowHeight) - (windowHeight * margin_top_percentage))));
        bar_colors.push(color('white'));
    }
}

function draw_bars() {
    for (var i = 0; i < num_bars; i++) {
        stroke(color('black'));
        fill(bar_colors[i]);
        rect(i * bar_width, height - bar_heights[i], bar_width, bar_heights[i]);
    }
}

function windowResized() {
    if (!currently_sorting) {
        bar_width = windowWidth / num_bars;
        generate_heights();
        resizeCanvas(windowWidth, windowHeight);
    }
}
