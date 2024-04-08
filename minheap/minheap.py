# A class for a min heap
class MinHeap:
    #Initializes the heap as empty. Insert elements from passed list to the heap if the list is not empty.
    def __init__(self, arr=[]):
        self.min_heap = []

        if len(arr) > 0:
            for i in arr:
                self.insert(i)
                
    #This function returns the index of the parent node of a given index
    def parent_idx(self, n):
        return (n - 1) // 2 #The parent index of a given index (excluding root) is at (n - 1) / 2
    
    #This function returns the index of the left child node of a given index
    def left_idx(self, n):
        return (n * 2) + 1 #The left child node of a give index is located at (n * 2) + 1

    #This function returns the index of the right child node of a given index
    def right_idx(self, n):
        return (n * 2) + 2 #The right child node of a give index is located at (n * 2) + 2

    #Heapify the node at given index n. The final result is a min heap
    def min_heapify(self, n):
        left_child = self.left_idx(n)
        right_child = self.right_idx(n)
        min_idx = n

        #Bound check left child node and check to see which is the lower value between parent node and left child node.
        if left_child < len(self) and self.min_heap[left_child] < self.min_heap[n]:
            min_idx = left_child

        #Bound check right child node and check to see which is the lower value between node at min_idx and right child node.
        if right_child < len(self) and self.min_heap[right_child] < self.min_heap[min_idx]:
            min_idx = right_child

        #min_idx by default is set to given index, if min_idx value changes then it indicates the order needs to swapped in the heap
        if min_idx != n:
            self.min_heap[n], self.min_heap[min_idx] = self.min_heap[min_idx], self.min_heap[n]
            self.min_heapify(min_idx) #Recursive call to heapify subtree

    #Adds the given element to the heap and heapifying it for correct order from bottom up
    def insert(self, element):
        self.min_heap.append(element)
        if len(self) > 1:
            curr_idx = self.parent_idx(len(self) - 1)
            while curr_idx >= 0:
                self.min_heapify(curr_idx)
                curr_idx = self.parent_idx(curr_idx)
    
    #Returns the root value which will always be the minimum value, returns None if the heap is empty
    def get_min(self):
        if len(self) == 0:
            return None
        else:
            return self.min_heap[0]

    #Stores the minimum value in a local variable then removes the minimum value from the heap. 
    #The local variable holding the minimum value is return, None is returned if the heap is empty
    def extract_min(self):
        if not self.is_empty():
            min_val = self.min_heap[0]

            if len(self) > 1:
                self.min_heap[0] = self.min_heap.pop()
                self.min_heapify(0)
            else:
                self.min_heap.pop()

            return min_val
        else:
            return None

    #Returns True if the there are no elements in the heap, returns False if there are elements in the heap
    def is_empty(self):
        if len(self) == 0:
            return True
        else:
            return False
    
    #Returns the number of elements in the heap
    def __len__(self):
        return len(self.min_heap)
