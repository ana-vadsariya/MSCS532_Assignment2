import random
import time
from memory_profiler import memory_usage


# Quick Sort Implementation Using Recusion
def quick_sort(arr):
    #Base case which stops the recursion when length of array becomes 1 or 0.
    if len(arr) <= 1:
        return arr
    #Randomly select pivot from the array starting at position 0 till the last element
    pivot = arr[random.randint(0, len(arr) - 1)]
    #all the values smaller than pivot goes to left_Side list
    left_side = [x for x in arr if x < pivot]
    #here is the pivot
    pivot_valeu = [x for x in arr if x == pivot]
    #all the values greater than pivot goes to right_Side list
    right_side = [x for x in arr if x > pivot]
    #now we send the left_side + pivot + right_side back to the recursion
    return quick_sort(left_side) + pivot_valeu + quick_sort(right_side)

# Merge Sort Implementation Using Recusion
def merge_sort(arr):
    #Base case which stops the recursion when length of array becomes 1 or 0.
    if len(arr) <= 1:
        return arr 
    # Divide the array into two equally parts 
    mid = len(arr) // 2
    #Extract the values before mid-point and add it to left_side array 
    left_side = arr[:mid]
    #Extract the values after mid-point and add it to right_side array 
    right_side = arr[mid:]
    #send both sides to the recursion level and store then in their respective variables
    left_sorted = merge_sort(left_side)
    right_sorted = merge_sort(right_side)
    # Merge the two sorted halves
    return merge(left_sorted, right_sorted)

#Merge step
def merge(left, right):
    merged = []
    i = j = 0
    # Merge the two lists in sorted order
    while i < len(left) and j < len(right):
        #Comparison is done to idenitfy which element to add next in the array
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    # Append any remaining elements from both halves
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def print_array(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()

# Measure execution time of a function 
def measure_time(func, arr):
    start_time = time.time()
    result = func(arr)
    end_time = time.time()
    return result, end_time - start_time

# Measure memory usage of a function
def measure_memory(func, arr):
    mem_usage = memory_usage((func, (arr,)))
    return max(mem_usage) - min(mem_usage)

def test_sorting_algorithms():
    array_sorted = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    array_reverse_sorted = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    array_random = random.sample(range(1, 10000), 1000)  

    #Quick Sort for sorted array
    quick_sorted, quick_time = measure_time(quick_sort, array_sorted)
    quick_mem = measure_memory(quick_sort, array_sorted)
    print("Sorted Array using Quick Sort") 
    print("Quick Sort Time:", quick_time, "seconds")
    print("Quick Sort Memory Usage:", quick_mem, "MiB")
    print()
        
    #Merge Sort for sorted array
    merge_sorted, merge_time = measure_time(merge_sort, array_sorted)
    merge_mem = measure_memory(merge_sort, array_sorted)
    print("Sorted Array using Merge Sort") 
    print("Merge Sort Time:", merge_time, "seconds")
    print("Merge Sort Memory Usage:", merge_mem, "MiB")
    print()

    #Quick Sort for reverse sorted array
    quick_sorted, quick_time = measure_time(quick_sort, array_reverse_sorted)
    quick_mem = measure_memory(quick_sort, array_reverse_sorted)
    print("Sorted Reverse Array using Quick Sort") 
    print("Quick Sort Time:", quick_time, "seconds")
    print("Quick Sort Memory Usage:", quick_mem, "MiB")
    print()


    #Merge Sort for reverse sorted array
    merge_sorted, quick_time = measure_time(quick_sort, array_reverse_sorted)
    merge_mem = measure_memory(merge_sort, array_reverse_sorted)
    print("Sorted Reverse Array using Merge Sort") 
    print("Quick Sort Time:", quick_time, "seconds")
    print("Quick Sort Memory Usage:", quick_mem, "MiB")
    print()

    #Quick Sort for random array
    quick_sorted, quick_time = measure_time(quick_sort, array_random)
    quick_mem = measure_memory(quick_sort, array_random)
    print("Sorted Random Array of size 1000 using Quick Sort") 
    print("Quick Sort Time:", quick_time, "seconds")
    print("Quick Sort Memory Usage:", quick_mem, "MiB")
    print()
        
    #Merge Sort for sorted array
    merge_sorted, merge_time = measure_time(merge_sort, array_random)
    merge_mem = measure_memory(merge_sort, array_random)
    print("Sorted Random Array of size 1000 using Merge Sort") 
    print("Merge Sort Time:", merge_time, "seconds")
    print("Merge Sort Memory Usage:", merge_mem, "MiB")
    print()
 
#used for memory calculation
if __name__ == '__main__':
    test_sorting_algorithms()






