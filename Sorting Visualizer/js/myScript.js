var margin_top_percentage = 0.3;
var num_bars = 200;
var bar_color = 255;
var bar_width;
var bar_heights = [];
var bar_colors = [];
var bar_color_width = 10;
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
        $('#start-button').attr('disabled', true);
        $('#new-button').attr('disabled', true);
        $('#num-bars-range').attr('disabled', true);
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

function apply_colors(initial_idx, limit_idx, bars_to_fill, color){
    for(var i = initial_idx; i < initial_idx + bars_to_fill; i++){
        if(i < limit_idx){
            bar_colors[i] = color;
        } else{
            break;
        }
    }
}

async function bubble_sort() {
    for (var i = 0; i < num_bars; i++) {
        var swapped = false;
        for (var j = 0; j < num_bars - i - 1; j++) {
            apply_colors(j, num_bars - i, bar_color_width, 'red');
            if (bar_heights[j] > bar_heights[j + 1]) {
                swap(j, j + 1);
                swapped = true;
            }
            await sleep(4); // 4 ms is the smallest delay possible using setTimeout()
            apply_colors(j, num_bars - i, bar_color_width, 'white');
        }
        if(!swapped){
            return;
        }
    }
    $('#new-button').removeAttr('disabled');
    $('#num-bars-range').removeAttr('disabled');
}

async function selection_sort() {
    for (var i = 0; i < num_bars; i++) {
        var min_idx = i;
        for (var j = i; j < num_bars; j++) {
            apply_colors(j, num_bars, bar_color_width, 'red');
            if (bar_heights[j] < bar_heights[min_idx]) {
                await sleep(4);
                min_idx = j;
            }
            apply_colors(j, num_bars, bar_color_width, 'white');
        }
        swap(i, min_idx);
    }
    $('#new-button').removeAttr('disabled');
    $('#num-bars-range').removeAttr('disabled');
}

async function insertion_sort() {
    for (var i = 1; i < num_bars; i++) {
        var current = i;
        var value = bar_heights[i];
        while (current > 0 && bar_heights[current - 1] > value) {
            bar_heights[current] = bar_heights[current - 1];
            current--;
        }
        await sleep(4);
        bar_heights[current] = value;
    }
    $('#new-button').removeAttr('disabled');
    $('#num-bars-range').removeAttr('disabled');
}

async function partition(start, end) {
    var pivot = bar_heights[end];
    var partn_idx = start;
    for (var i = start; i < end; i++) {
        if (bar_heights[i] <= pivot) {
            await sleep(4);
            await swap(i, partn_idx)
            partn_idx++;
        }
    }
    await swap(partn_idx, end);
    return partn_idx;
}

async function quick_sort_lomuto(start = 0, end = num_bars - 1) {
    if (start < end) {
        var partn_idx = await partition(start, end);
        await Promise.all([
            quick_sort_lomuto(start, partn_idx - 1),
            quick_sort_lomuto(partn_idx + 1, end)
        ]);
    } else {
        $('#new-button').removeAttr('disabled');
        $('#num-bars-range').removeAttr('disabled');
    }
}

    function merge_sort(arr = bar_heights) {
    if (arr.length <= 1) {
        return arr;
        }
        var mid = Math.round((arr.length / 2));
        var left = arr.slice(0, mid);
        var right = arr.slice(mid);
        return merge(merge_sort(left), merge_sort(right));
}

function merge(left, right) {
    sorted = [];
    while (left && left.length > 0 && right && right.length > 0) {
        if (left[0] <= right[0]) {
            sorted.push(left.shift());
        } else {
            sorted.push(right.shift());
        }
    }
    bar_heights = sorted.concat(left, right);
    return bar_heights;
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

function swap(x, y) {
    var temp = bar_heights[x];
    bar_heights[x] = bar_heights[y];
    bar_heights[y] = temp;
}

function windowResized() {
    if (!currently_sorting) {
        bar_width = windowWidth / num_bars;
        generate_heights();
        resizeCanvas(windowWidth, windowHeight);
    }
}
