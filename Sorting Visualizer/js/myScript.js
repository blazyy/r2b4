// Note to self: Paperscript doesn't support ES6, so I can't use let/const and other ES6 stuff.
var margin_top_percentage = 0.1;
var window_height = ($(window).height() - ($(window).height() * margin_top_percentage));
var window_width = $(window).width();
var num_bars = 400;
var bar_color = '#ffffff';
var increment = window_width / num_bars;
var bar_heights = [];

function generate_heights(){
    bar_heights = [];
    for(var i = 0; i < num_bars; i++){
        bar_heights.push(Math.floor(Math.random() * window_height + 1));
    }
}

var bubble_sort = function(arr){
    for(var i = 0; i < num_bars; i++){
        console.log(arr[i]);
        for(var j = 0; j < (num_bars - i - 1); j++){
            if(arr[j] > arr[j+1]){
                var temp = arr[j+1];
                arr[j+1] = arr[j];
                arr[j] = temp;
                project.activeLayer.removeChildren(); // Removes drawn bars
                draw_bars();
            }
        }
    }
}

function draw_bars(){
    width_pen = 0;
    for(var i = 0; i < num_bars; i++){
        bottom_left = new Point(width_pen, bar_heights[i]);
        width_pen += increment;
        top_right = new Point(width_pen, 0);
        rect = new Rectangle(bottom_left, top_right);
        path = new Path.Rectangle(rect);
        path.fillColor = bar_color;
        path.strokeColor = bar_color
    }
}

bubble_sort(bar_heights);

// Whenever the window is resized, function executes
function onResize(event) {
    window_height = ($(window).height() - ($(window).height() * margin_top_percentage));
    window_width = $(window).width();
    increment = window_width / num_bars
    project.activeLayer.removeChildren(); // Removes drawn bars
    generate_heights();
    draw_bars();
}
