"""
Okkar Kaung Myat
6632104
542
"""
class MinHeap:
    def __init__(self):
        self.heap = []

    def __len__(self):
        return len(self.heap)
    
    def insert(self, value):
        self.heap.append(value)

        index = len(self.heap) - 1
        while index > 0:
            # find parent's index with heap formula
            parent = (index - 1) // 2
            
            # stop if heap property satisfied 
            if self.heap[parent] <= self.heap[index]:
                break

            # python support tuple unpacking(parallel assignment)
            # self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            # index = parent
            temp = self.heap[parent]
            self.heap[parent] = self.heap[index]
            self.heap[index] = temp
            index = parent

    def pop(self):
        root = self.heap[0]

        # remove the last element: cannot be empty at index 0
        last = self.heap.pop()

        if self.heap:
            self.heap[0] = last # move last element to root
            self.sift_down(0) # restore heap property
            
        return root

    def peek(self):
        return self.heap[0] # return minimum value

    # helper
    def sift_down(self, index):
        size = len(self.heap)

        while True:
            # complete binary tree: children positions can be computed using simple heap formulas.
            left = (2 * index) + 1
            right = (2 * index) + 2
            smallest = index

            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left

            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == index:
                break

            # self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            # index = smallest
            temp = self.heap[index]
            self.heap[index] = self.heap[smallest]
            self.heap[smallest] = temp
            index = smallest

def findKthLargest(nums, k):
    heap = MinHeap()
    for x in nums:
        heap.insert(x)
        # if len(heap.heap) > k:
        if len(heap) > k:
            heap.pop()
    return heap.peek()

# print(findKthLargest([3, 2, 1, 5, 6, 4], 2))
print(findKthLargest([3,2,3,1,2,4,5,5,6], 4))