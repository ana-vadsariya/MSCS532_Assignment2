import random

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

#Provided array to be sorted
array = [1, 12, 3, 44, 5, 6]

#print before sorting
print("Given Array")  
print_array(array)

#perform the sorting
quick_sorted_array = quick_sort(array)

print("Sorted Array using Quick Sort") 
print_array(quick_sorted_array) 

merge_sorted_array = merge_sort(array)
print("Sorted Array using Merge Sort")
print_array(merge_sorted_array) 






