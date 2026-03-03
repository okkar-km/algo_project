"""
Okkar Kaung Myat
6632104
542
"""
import random
def partition(arr, low, high):
    
    # choose the pivot
    # pivot = arr[high]
    pivot_idx = random.randint(low, high)
    swap(arr, pivot_idx, high)

    pivot = arr[high]
    
    # index of smaller element and indicates the right position of pivot found so far
    i = low - 1
    
    # traverse arr[low..high] and move all smaller elements to the left side. Elements from low to 
    # i are smaller after every iteration
    for j in range(low, high):
        if arr[j] < pivot: # ascending order
            i += 1
            swap(arr, i, j)
    
    # move pivot after smaller elements and return its position
    swap(arr, i + 1, high)
    return i + 1

# swap function
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

# the QuickSort function implementation
# Quickselect Ascending
def quickSelect(arr, low, high, target):
    # if low < high:
        
    #     # pi is the partition return index of pivot
    #     pi = partition(arr, low, high)
        
    #     # recursion calls for smaller elements
    #     # and greater or equals elements
    #     quickSort(arr, low, pi - 1)
    #     quickSort(arr, pi + 1, high)

    if low == high:
        return arr[low]
    
    pi = partition(arr, low, high)

    if pi == target:
        return arr[pi]
    elif pi > target:
        return quickSelect(arr, low, pi-1, target)
    else:
        return quickSelect(arr, pi+1, high, target)
    
def findKthLargest(nums, k):
    n = len(nums)
    target = n - k 
    return quickSelect(nums, 0, n-1, target)
    
print(findKthLargest([3, 2, 1, 5, 6, 4], 2))
