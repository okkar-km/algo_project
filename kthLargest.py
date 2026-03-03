"""
Okkar Kaung Myat
6632104
542
"""
# def findKthLargest(nums, k):
#     nums.sort(reverse=True)
#     return nums[k - 1]

# print(findKthLargest([3, 2, 1, 5, 6, 4], 2))
# print(findKthLargest([3, 2, 1, 5, 6, 4], 5))

import heapq
from typing import List

# def findKthLargest(nums: List[int], k: int) -> int:
#     heap = []
#     for x in nums:
#         heapq.heappush(heap, x)
#         if len(heap) > k:
#             heapq.heappop(heap)   # remove smallest among current top-k
#     return heap[0]  # smallest in heap == kth largest overall

def insert(heap, value):
    # Add the new element to the end of the heap
    heap.append(value)
    
    # Get the index of the last element
    index = len(heap) - 1
    # Compare the new element with
    # its parent and swap if necessary
    while index > 0 and heap[(index - 1) // 2] > heap[index]:
        heap[index], heap[(index - 1) // 2] = heap[(index - 1) // 2], heap[index]
        # Move up the tree to the
        # parent of the current element
        index = (index - 1) // 2

# Function to delete a node from the min-heap
def deleteMin(heap, value):
    # Find the index of the element to be deleted
    index = -1
    for i in range(len(heap)):
        if heap[i] == value:
            index = i
            break

    # If the element is not found, return
    if index == -1:
        return

    # Replace the element to be deleted with the last
    # element
    heap[index] = heap[-1]

    # Remove the last element
    heap.pop()

    # Heapify the tree starting from the element at the
    # deleted index
    while True:
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        smallest = index

        if left_child < len(heap) and heap[left_child] < heap[smallest]:
            smallest = left_child
        if right_child < len(heap) and heap[right_child] < heap[smallest]:
            smallest = right_child

        if smallest != index:
            heap[index], heap[smallest] = heap[smallest], heap[index]
            index = smallest
        else:
            break

def top(heap):
    if heap:
        # Root element
        return heap[0]
    return -1

def heapify(arr, i, n):
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2

    # If left child exists and is smaller than root
    if l < n and arr[l] < arr[smallest]:
        smallest = l

    # If right child exists and is smaller than smallest so far
    if r < n and arr[r] < arr[smallest]:
        smallest = r

    # If smallest is not root,
    # swap and continue heapifying
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        # Recursively heapify
        heapify(arr, smallest, n)