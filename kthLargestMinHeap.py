"""
Okkar Kaung Myat
6632104
542
"""
from typing import List
class MinHeap:
    def __init__(self):
        self.heap = []

    def __len__(self):
        return len(self.heap)
    
    def push(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, index):
        while index > 0:
            # find parent's index with heap formula
            parent = (index - 1) // 2

            # stop if heap property satisfied 
            if self.heap[parent] <= self.heap[index]:
                break

            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            index = parent

    def pop(self):
        root = self.heap[0]

        # remove the last element: cannot be empty at index 0
        last = self.heap.pop()

        if self.heap:
            self.heap[0] = last # move last element to root
            self.heapify_down(0) # restore heap property
            
        return root

    def heapify_down(self, index):
        size = len(self.heap)

        while True:
            # complete binary tree: children positions are computed using simple heap formulas.
            left = (2 * index) + 1
            right = (2 * index) + 2
            smallest = index

            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left

            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == index:
                break

            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest

    def peek(self):
        return self.heap[0] # return minimum value

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = MinHeap()
        for x in nums:
            heap.push(x)
            if len(heap) > k:
                heap.pop()
        return heap.peek()

sol = Solution()
print(sol.findKthLargest([3,2,3,1,2,4,5,5,6], 4))