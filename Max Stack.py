class MaxStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.maxHeap = []
        self.toPop_heap = {}  # to keep track of things to remove from the heap
        self.toPop_stack = set()  # to keep track of things to remove from the stack

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        heapq.heappush(self.maxHeap, (-x, -len(self.stack)))
        self.stack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        self.top()
        x = self.stack.pop()
        key = (-x, -len(self.stack))
        self.toPop_heap[key] = self.toPop_heap.get(key, 0) + 1
        return x

    def top(self):
        """
        :rtype: int
        """
        while self.stack and len(self.stack) - 1 in self.toPop_stack:
            x = self.stack.pop()
            self.toPop_stack.remove(len(self.stack))
        return self.stack[-1]

    def peekMax(self):
        """
        :rtype: int
        """
        while self.maxHeap and self.toPop_heap.get(self.maxHeap[0], 0):
            x = heapq.heappop(self.maxHeap)
            self.toPop_heap[x] -= 1
        return -self.maxHeap[0][0]

    def popMax(self):
        """
        :rtype: int
        """
        self.peekMax()
        x, idx = heapq.heappop(self.maxHeap)
        x, idx = -x, -idx
        self.toPop_stack.add(idx)
        return x