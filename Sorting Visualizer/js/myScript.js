// Note to self: Paperscript doesn't support ES6, so I can't use let/const and other ES6 stuff.
var margin_top_percentage = 0.1;
var window_height = ($(window).height() - ($(window).height() * margin_top_percentage));
var window_width = $(window).width();
var num_bars = 100;
var bar_color = '#ffffff';
var increment = window_width / num_bars;
var bar_heights = [];
var initial_resize = true;

function clear_screen(){
    project.activeLayer.removeChildren(); // Removes drawn bars
}

function generate_heights(){
    bar_heights = [];
    for(var i = 0; i < num_bars; i++){
        bar_heights.push(Math.floor(Math.random() * window_height + 1));
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

function bubble_sort(){
    for(var i = 0; i < num_bars; i++){
        for(var j = 0; j < num_bars - i - 1; j++){
            if(bar_heights[j] > bar_heights[j+1]){
                var temp = bar_heights[j];
                bar_heights[j] = bar_heights[j+1];
                bar_heights[j+1] = temp;
            }
        }
    }
}

function onResize(event) {
    // Need this flag because onResize was getting called when the page initially loaded, which I don't want.
    if(!initial_resize){
        console.log("RESIZE");
        initial_resize = false;
        window_height = ($(window).height() - ($(window).height() * margin_top_percentage));
        window_width = $(window).width();
        increment = window_width / num_bars
        clear_screen(); // Removes drawn bars
        generate_heights();
        draw_bars();
    }
}

generate_heights();
draw_bars();
console.log('before: ', bar_heights);
// Javascript sorts alphabetically by default. To get it to sort numbers, I have to do this weird trick which doesn't make any sense.
// bar_heights.sort(function(a, b){
//     return a-b;
// });
bubble_sort();
draw_bars();
console.log('after: ', bar_heights);
