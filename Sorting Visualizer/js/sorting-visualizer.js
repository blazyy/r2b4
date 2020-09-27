const margin_top_percentage = 0.5,
    bar_color = 255,
    available_sorts = {
        'bubble': bubble_sort,
        'cocktail': cocktail_shaker_sort,
        'selection': selection_sort,
        'insertion': insertion_sort,
        'shell': shell_sort,
        'quicksort_l': quick_sort_lomuto,
        'quicksort_h': quick_sort_hoare,
        'merge': merge_sort
    };

let colored_bars = true,
    num_bars = 150,
    bar_width,
    bar_color_width = 2,
    currently_sorting = false,
    stopped = false,
    selected_sort = 'bubble',
    bar_heights = [], // Didn't make this const since merge sort needs the array to be reassignable
    bar_colors = [], // same
    old_window_width;

function setup() {
    frameRate(60);
    createCanvas(windowWidth, windowHeight);
    old_window_width = windowWidth;
    bar_width = windowWidth / num_bars;
    generate_heights_and_color_in();
    draw_bars();
    noLoop();
}

function draw() {
    background(0);
    draw_bars();
}

function draw_bars() {
    for (let i = 0; i < num_bars; i++) {
        stroke(color('black'));
        fill(bar_colors[i]);
        rect(i * bar_width, height - bar_heights[i], bar_width, bar_heights[i]);
    }
}

function generate_heights_and_color_in() {
    bar_heights.splice(0, bar_heights.length);
    for (let i = 0; i < num_bars; i++)
        bar_heights.push(Math.floor(Math.random() * (windowHeight - (windowHeight * margin_top_percentage))));
    set_bar_colors();
}

function set_bar_colors() {
    bar_colors.splice(0, bar_colors.length); // empties array
    if (colored_bars) {
        // let rainbow = chroma.scale(['yellow', 'navy']).mode('lch').domain([0, Math.max(...bar_heights)]);
        let rainbow = chroma.scale(['yellow', 'red', 'black']).domain([0, Math.max(...bar_heights)]);
        for (let i = 0; i < num_bars; i++) {
            let new_color = rainbow(bar_heights[i]),
                r = Math.floor(new_color._rgb[0]),
                g = Math.floor(new_color._rgb[1]),
                b = Math.floor(new_color._rgb[2]);
            bar_colors.push(color(r, g, b));
        }
    } else {
        for (let i = 0; i < num_bars; i++) {
            bar_colors.push(color('white'));
        }
    }
    loop();
    noLoop();
}

function windowResized() {
    old_window_width = windowWidth;
    redraw_bars(resize = true);
}

function redraw_bars(resize = false) {
    if (!currently_sorting) {
        $('#start-button').removeAttr('disabled');
        bar_width = windowWidth / num_bars;
        generate_heights_and_color_in();
        if (resize)
            resizeCanvas(windowWidth, windowHeight);
    }
}

$(document).ready(function() {
    initialize();
});

function initialize() {
    $('#num-bars-range').on('input', function() {
        num_bars = $(this).val();
        redraw_bars();
    });

    $('#sort-select-dropdown').on('change', function() {
        selected_sort = $(this).val();
    });

    $('#color-toggle-switch').on('change', function() {
        $('#color-toggle-switch').is(':checked') ? colored_bars = true : colored_bars = false;
        set_bar_colors();
    });

    $('#start-button').on('click', async function() {
        $('#start-button, #num-bars-range, #new-button, #sort-select-dropdown, #color-toggle-switch').attr('disabled', true);
        $('#reset-button').removeAttr('disabled');
        currently_sorting = true;
        loop();
        await available_sorts[selected_sort]();
        noLoop();
        currently_sorting = false;
        $('#sort-select-dropdown, #new-button, #num-bars-range, #color-toggle-switch').removeAttr('disabled');
    });

    $('#new-button').on('click', () => redraw_bars(resize = true));

    $('#reset-button').on('click', () => window.location.reload());
}