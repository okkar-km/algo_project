"""
Okkar Kaung Myat
6632104
542
"""
# for extremely unbalanced partitons due to massive duplicates, three way partitions with iterative approach to avoid recursion depth issues
import random
def partition(arr, low, high):
    
    pivot = arr[random.randint(low, high)]
    lt = low # end of less than
    gt = high # start of greater than
    i = low # current index

    while i <= gt:
        if arr[i] < pivot:
            arr[lt], arr[i] = arr[i] , arr[lt]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            arr[gt], arr[i] = arr[i], arr[gt]
            gt -= 1
        else: 
            i += 1
    return lt, gt

# the QuickSort function implementation
# Quickselect Ascending
def quickSelect(arr, low, high, target):

    while low <= high:
        lt, gt = partition(arr, low, high)

        if target < lt:
            high = lt - 1
        elif target > gt:
            low = gt + 1
        else:
            return arr[target]

def findKthLargest(nums, k):
    n = len(nums)
    target = n - k 
    return quickSelect(nums, 0, n-1, target)
    
print(findKthLargest([3,2,3,1,2,4,5,5,6], 4))
