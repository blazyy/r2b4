function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

function swap(x, y) {
    var temp = bar_heights[x];
    bar_heights[x] = bar_heights[y];
    bar_heights[y] = temp;
}

function apply_colors(initial_idx, limit_idx, bars_to_fill, color, algorithm) {
    if (algorithm === 'bubble' || algorithm === 'selection') {
        for (var i = initial_idx; i < initial_idx + bars_to_fill; i++) {
            if (i < limit_idx) {
                bar_colors[i] = color;
            } else {
                break;
            }
        }
    } else if (algorithm === 'insertion') {
        for (var i = initial_idx; i >= initial_idx - bars_to_fill; i--) {
            bar_colors[i] = color;
        }
    }
}

async function bubble_sort() {
    for (var i = 0; i < num_bars; i++) {
        var swapped = false;
        for (var j = 0; j < num_bars - i - 1; j++) {
            apply_colors(j, num_bars - i, bar_color_width, 'red', 'bubble');
            if (bar_heights[j] > bar_heights[j + 1]) {
                swap(j, j + 1);
                swapped = true;
            }
            await sleep(4); // 4 ms is the smallest delay possible using setTimeout(). This is a browser limitation.
            apply_colors(j, num_bars - i, bar_color_width, 'white', 'bubble');
        }
        if (!swapped) {
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
            apply_colors(j, num_bars, bar_color_width, 'red', 'selection');
            if (bar_heights[j] < bar_heights[min_idx]) {
                min_idx = j;
                await sleep(4);
            }
            apply_colors(j, num_bars, bar_color_width, 'white', 'selection');
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
            apply_colors(current, 0, bar_color_width, 'red', 'insertion');
            bar_heights[current] = bar_heights[current - 1];
            await sleep(4);
            apply_colors(current, 0, bar_color_width, 'white', 'insertion');
            current--;
        }
        bar_heights[current] = value;
    }
    $('#new-button').removeAttr('disabled');
    $('#num-bars-range').removeAttr('disabled');
}

async function partition(start, end) {
    var pivot = bar_heights[end];
    var partn_idx = start;
    for (var i = start; i < end; i++) {
        apply_colors(i, 0, bar_color_width, 'red', 'quick');
        if (bar_heights[i] <= pivot) {
            await sleep(4);
            await swap(i, partn_idx)
            partn_idx++;
        }
        apply_colors(i, 0, bar_color_width, 'white', 'quick');
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
