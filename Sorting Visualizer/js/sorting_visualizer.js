const margin_top_percentage = 0.5;
const bar_color = 255;
const bar_heights = [];
const bar_colors = [];
const available_sorts = {
    'bubble': bubble_sort,
    'selection': selection_sort,
    'quicksort_l': quick_sort_lomuto,
    'quicksort_h': quick_sort_hoare,
    'insertion': insertion_sort,
    'merge': merge_sort
}

let num_bars = 200;
let bar_width;
let bar_color_width = 2;
let currently_sorting = false;
let stopped = false;
let selected_sort = 'bubble';

function setup() {
    frameRate(60);
    createCanvas(windowWidth, windowHeight);
    bar_width = windowWidth / num_bars;
    generate_heights();
}

function draw() {
    background(0);
    for (let i = 0; i < num_bars; i++) {
        stroke(color('black'));
        fill(bar_colors[i]);
        rect(i * bar_width, height - bar_heights[i], bar_width, bar_heights[i]);
    }
}

function generate_heights() {
    bar_heights.splice(0, bar_heights.length); // empties array
    for (let i = 0; i < num_bars; i++) {
        bar_heights.push(Math.floor(Math.random() * (windowHeight - (windowHeight * margin_top_percentage))));
        bar_colors.push(color('white'));
    }
}

function windowResized() {
    if (!currently_sorting) {
        bar_width = windowWidth / num_bars;
        generate_heights();
        resizeCanvas(windowWidth, windowHeight);
    }
}

$(document).ready(function() {
    initialize();
});

function initialize() {
    $('#start-button').on('click', async function() {
        $('#start-button, #num-bars-range, #new-button, #sort-select-dropdown').attr('disabled', true);
        $('#reset-button').removeAttr('disabled');
        await available_sorts[selected_sort]();
        $('#sort-select-dropdown, #new-button, #num-bars-range').removeAttr('disabled');
    });

    $('#new-button').on('click', () => {
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

    $('#reset-button').on('click', () => window.location.reload());
}