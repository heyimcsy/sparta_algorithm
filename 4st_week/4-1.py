def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_and_sort_arrays(arr1, arr2):
    merged_array = arr1 + arr2
    sorted_array = quick_sort(merged_array)
    return sorted_array

arr1 = [10, 5, 15]
arr2 = [4, 11, 2]
print(merge_and_sort_arrays(arr1, arr2))