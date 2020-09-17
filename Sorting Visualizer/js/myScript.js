// Note to self: Paperscript doesn't support ES6, so I can't use let/const and other ES6 stuff.
var window_height = $(window).height();
var window_width = $(window).width();
var num_bars = 300;
var increment = window_width / num_bars;
var bar_heights = []

function draw_bars(window_height, window_width){
    bar_heights = [];
    for(var i = 0; i < num_bars; i++){
        bar_heights.push(Math.floor(Math.random() * window_height + 1));
    }
    width_pen = 0;
    for(var i = 0; i < num_bars; i++){
        bottom_left = new Point(width_pen, bar_heights[i]);
        width_pen += increment;
        top_right = new Point(width_pen, 0);
        rect = new Rectangle(bottom_left, top_right);
        path = new Path.Rectangle(rect);
        path.fillColor = '#ffffff';
        path.strokeColor = '#ffffff'
    }
}

draw_bars(window_height, window_width);

// Whenever the window is resized, function executes
function onResize(event) {
    window_height = $(window).height();
    window_width = $(window).width();
    draw_bars(window_height, window_width);
}
