import random

def partition_hoare(start, end):
	pivot = arr[start]
	i = start - 1
	j = end + 1
	while True:
		i += 1
		while arr[i] < pivot:
			i += 1
		j -= 1
		while arr[j] > pivot:
			j -= 1
		if i >= j:
			return j
		arr[i], arr[j] = arr[j], arr[i]

def quick_sort_hoare(start, end):
	if start < end:
		p_index = partition_hoare(start, end)
		quick_sort_hoare(start, p_index)
		quick_sort_hoare(p_index + 1, end)

arr = [random.randint(1, 100) for i in range(15)]
print(arr)
quick_sort_hoare(0, len(arr) - 1)
print(arr)
