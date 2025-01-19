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
sorted_array = quick_sort(array)
print("Sorted Array")  
print_array(sorted_array)


