function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

function swap(x, y) {
    var temp = bar_heights[x];
    bar_heights[x] = bar_heights[y];
    bar_heights[y] = temp;
}

function apply_colors(initial_idx, limit_idx, bars_to_fill, color, algorithm) {
    if (algorithm === 'bubble' || algorithm === 'selection' || algorithm === 'quick_l' || algorithm === 'quick_h' || algorithm === 'merge') {
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

async function partition_lomuto(start, end) {
    var pivot = bar_heights[end];
    var partn_idx = start;
    for (var i = start; i < end; i++) {
        if (bar_heights[i] <= pivot) {
            apply_colors(i, end, bar_color_width, 'red', 'quick_l');
            await sleep(4);
            swap(i, partn_idx);
            partn_idx++;
            apply_colors(i, end, bar_color_width, 'white', 'quick_l');
        }
    }
    swap(partn_idx, end);
    return partn_idx;
}

async function quick_sort_lomuto(start = 0, end = num_bars - 1) {
    if (start < end) {
        var partn_idx = await partition_lomuto(start, end);
        await quick_sort_lomuto(start, partn_idx - 1);
        await quick_sort_lomuto(partn_idx + 1, end);
    } else {
        $('#new-button').removeAttr('disabled');
        $('#num-bars-range').removeAttr('disabled');
    }
}

async function partition_hoare(start, end) {
    var pivot = bar_heights[start];
    var i = start - 1;
    var j = end + 1;
    while (true) {
        i++;
        while (bar_heights[i] < pivot) {
            i++;
        }
        j--;
        while (bar_heights[j] > pivot) {
            j--;
        }
        if (i >= j) {
            return j;
        }
        apply_colors(i, end, bar_color_width, 'red', 'quick_h');
        apply_colors(j, end, bar_color_width, 'red', 'quick_h');
        await sleep(4);
        apply_colors(i, end, bar_color_width, 'white', 'quick_h');
        apply_colors(j, end, bar_color_width, 'white', 'quick_h');
        swap(i, j);
    }
}

async function quick_sort_hoare(start = 0, end = num_bars - 1) {
    if (start < end) {
        var partn_idx = await partition_hoare(start, end);
        await quick_sort_hoare(start, partn_idx);
        await quick_sort_hoare(partn_idx + 1, end);
    }
}

// I was finding it difficult to visualize merge sort since it's not an inplace algorithm
// Since merge sort creates auxiliary arrays, I had to do a bit of searching around
// I found the answer on StackOverflow, and with a little bit of modifying, I was able to make it work.
// What's different here is that we write back copies of the array into the original global array.
// Thank you, Rabbid76.

function merge_sort() {
    arr_copy = bar_heights.slice();
    merge_sort_slice(arr_copy, 0, num_bars);
    return;
}
async function merge_sort_slice(arr_copy, start, end) {
    if (end - start <= 1)
        return;
    var mid = Math.round((end + start) / 2);
    await merge_sort_slice(arr_copy, start, mid);
    await merge_sort_slice(arr_copy, mid, end);
    let i = start;
    let j = mid;
    while (i < end && j < end) {
        if (arr_copy[i] > arr_copy[j]) {
            let t = arr_copy[j];
            apply_colors(i, end, bar_color_width, 'red', 'merge');
            apply_colors(j, end, bar_color_width, 'red', 'merge');
            arr_copy.splice(j, 1);
            arr_copy.splice(i, 0, t);
            await sleep(20);
            apply_colors(i, end, bar_color_width, 'white', 'merge');
            apply_colors(j, end, bar_color_width, 'white', 'merge');
            j++;
        }
        i++;
        if (i == j)
            j++;
        // copy back the current state of the sorting
        bar_heights = arr_copy.slice();
    }
}