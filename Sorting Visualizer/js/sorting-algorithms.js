function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

function swap(x, y) {
    const temp1 = bar_heights[x];
    bar_heights[x] = bar_heights[y];
    bar_heights[y] = temp1;
    const temp2 = bar_colors[x];
    bar_colors[x] = bar_colors[y];
    bar_colors[y] = temp2;
}

function apply_colors(initial_idx, limit_idx, bars_to_fill, color, algorithm) {
    if (!colored_bars) {
        if (algorithm === 'insertion') {
            for (let i = initial_idx; i >= initial_idx - bars_to_fill; i--) {
                bar_colors[i] = color;
            }
        } else {
            for (let i = initial_idx; i < initial_idx + bars_to_fill; i++) {
                if (i < limit_idx) {
                    bar_colors[i] = color;
                } else {
                    break;
                }
            }
        }
    }
}

async function bubble_sort() {
    for (let i = 0; i < num_bars; i++) {
        let swapped = false;
        for (let j = 0; j < num_bars - i - 1; j++) {
            apply_colors(j, num_bars - i, bar_color_width, 'red', 'bubble');
            if (bar_heights[j] > bar_heights[j + 1]) {
                swap(j, j + 1);
                swapped = true;
            }
            await sleep(4); // 4 ms is the smallest delay possible using setTimeout(). This is a browser limitation.
            apply_colors(j, num_bars - i, bar_color_width, 'white', 'bubble');
        }
        if (!swapped) {
            break;
        }
    }
}

async function cocktail_shaker_sort() {
    let lower_limit = 0;
    let upper_limit = num_bars - 1;
    while (lower_limit < upper_limit) {
        let swapped_1 = false;
        let swapped_2 = false;
        for (let i = lower_limit; i < upper_limit; i++) {
            if (bar_heights[i] > bar_heights[i + 1]) {
                swap(i, i + 1);
                swapped_1 = true;
            }
            apply_colors(i, num_bars, bar_color_width, 'red', 'bubble');
            await sleep(4);
            apply_colors(i, num_bars, bar_color_width, 'white', 'bubble');
        }
        upper_limit--;
        for (let i = upper_limit; i > lower_limit; i--) {
            if (bar_heights[i] < bar_heights[i - 1]) {
                swap(i, i - 1);
                swapped_2 = true;
            }
            apply_colors(i, num_bars, bar_color_width, 'red', 'bubble');
            await sleep(4);
            apply_colors(i, num_bars, bar_color_width, 'white', 'bubble');
        }
        lower_limit++;
        if (!swapped_1 && !swapped_2)
            break;
    }
}

async function selection_sort() {
    for (let i = 0; i < num_bars; i++) {
        let min_idx = i;
        for (let j = i; j < num_bars; j++) {
            apply_colors(j, num_bars, bar_color_width, 'red', 'selection');
            if (bar_heights[j] < bar_heights[min_idx]) {
                min_idx = j;
                await sleep(20);
            }
            apply_colors(j, num_bars, bar_color_width, 'white', 'selection');
        }
        swap(i, min_idx);
    }
}

async function insertion_sort() {
    for (let i = 1; i < num_bars; i++) {
        let current = i;
        let value = bar_heights[i];
        let value_color = bar_colors[i];
        while (current > 0 && bar_heights[current - 1] > value) {
            apply_colors(current, 0, bar_color_width, 'red', 'insertion');
            bar_heights[current] = bar_heights[current - 1];
            bar_colors[current] = bar_colors[current - 1];
            await sleep(4);
            apply_colors(current, 0, bar_color_width, 'white', 'insertion');
            current--;
        }
        bar_heights[current] = value;
        bar_colors[current] = value_color;
    }
}

async function shell_sort() {
    let gap = Math.floor(num_bars / 2);
    while (gap > 0) {
        for (let i = gap; i < num_bars; i++) {
            let j = i;
            let temp = bar_heights[i];
            let temp_color = bar_colors[i];
            while (j >= gap && bar_heights[j - gap] > temp) {
                apply_colors(j, gap, bar_color_width, 'red', 'insertion');
                apply_colors(j - gap, gap, bar_color_width, 'red', 'insertion');
                bar_heights[j] = bar_heights[j - gap];
                bar_colors[j] = bar_colors[j - gap];
                await sleep(4);
                apply_colors(j, gap, bar_color_width, 'white', 'insertion');
                apply_colors(j - gap, gap, bar_color_width, 'white', 'insertion');
                j -= gap;
            }
            bar_heights[j] = temp;
            bar_colors[j] = temp_color;
        }
        gap = Math.floor(gap / 2);
    }
}

async function partition_lomuto(start, end) {
    let pivot = bar_heights[end];
    let partn_idx = start;
    for (let i = start; i < end; i++) {
        if (bar_heights[i] <= pivot) {
            apply_colors(i, end, bar_color_width, 'red', 'quick_l');
            await sleep(20);
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
        let partn_idx = await partition_lomuto(start, end);
        await quick_sort_lomuto(start, partn_idx - 1);
        await quick_sort_lomuto(partn_idx + 1, end);
    }
}

async function partition_hoare(start, end) {
    let pivot = bar_heights[start];
    let i = start - 1;
    let j = end + 1;
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
        await sleep(25);
        apply_colors(i, end, bar_color_width, 'white', 'quick_h');
        apply_colors(j, end, bar_color_width, 'white', 'quick_h');
        swap(i, j);
    }
}

async function quick_sort_hoare(start = 0, end = num_bars - 1) {
    if (start < end) {
        let partn_idx = await partition_hoare(start, end);
        await quick_sort_hoare(start, partn_idx);
        await quick_sort_hoare(partn_idx + 1, end);
    }
}

// I was finding it difficult to visualize merge sort since it's not an inplace algorithm
// Since merge sort creates auxiliary arrays, I had to do a bit of searching around
// I found the answer on StackOverflow, and with a little bit of modifying, I was able to make it work.
// What's different here is that we write back copies of the array into the original global array.
// Thank you, Rabbid76.

async function merge_sort() {
    let arr_copy = bar_heights.slice();
    let color_arr_copy = bar_colors.slice();
    await merge_sort_slice(arr_copy, color_arr_copy, 0, num_bars);
    return;
}

async function merge_sort_slice(arr, color_arr, start, end) {
    if (end - start <= 1)
        return;
    let mid = Math.round((end + start) / 2);
    await merge_sort_slice(arr, color_arr, start, mid);
    await merge_sort_slice(arr, color_arr, mid, end);
    let i = start;
    let j = mid;
    while (i < end && j < end) {
        if (arr[i] > arr[j]) {
            let t1 = arr[j];
            let t2 = color_arr[j];
            apply_colors(i, end, bar_color_width, 'red', 'merge');
            apply_colors(j, end, bar_color_width, 'red', 'merge');
            arr.splice(j, 1);
            color_arr.splice(j, 1);
            arr.splice(i, 0, t1);
            color_arr.splice(i, 0, t2);
            await sleep(20);
            apply_colors(i, end, bar_color_width, 'white', 'merge');
            apply_colors(j, end, bar_color_width, 'white', 'merge');
            j++;
        }
        i++;
        if (i == j)
            j++;
        // copy back the current state of the sorting
        bar_heights = arr.slice();
        bar_colors = color_arr.slice();
    }
}