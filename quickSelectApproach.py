"""
Okkar Kaung Myat
6632104
542
"""
import random
from typing import List

# swap function
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def partition(arr, low, high):
    # choose random pivot to avoid edge cases, then move pivot element to end
    pivot_idx = random.randint(low, high)
    swap(arr, pivot_idx, high)
    pivot = arr[high]
    
    # keep track of where the next smaller-than-pivot element should be placed
    store = low
    
    # traverse arr[low..high] and move all smaller elements to the left side. 
    # Elements from low to i are smaller after every iteration
    for j in range(low, high):
        if arr[j] < pivot: # ascending partition
            swap(arr, store, j)
            store += 1
    
    # move pivot after smaller elements and return its position
    swap(arr, store, high)
    return store

# the QuickSort function implementation
def quickSelect(arr, low, high, target):
    if low == high:
        return arr[low]
    
    pi = partition(arr, low, high)

    if pi == target:
        return arr[pi]
    elif pi > target:
        return quickSelect(arr, low, pi-1, target)
    else:
        return quickSelect(arr, pi+1, high, target)
    
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        target = n - k 
        return quickSelect(nums, 0, n-1, target)
    
sol = Solution()
print(sol.findKthLargest([3, 2, 1, 5, 6, 4], 2))
