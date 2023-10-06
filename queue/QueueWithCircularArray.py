class QueueWithCircularArray():
    def __init__(self, limit = 5):
        self.queue = [None] * limit
        self.limit = limit
        self.front = 0
        self.rear = 0
        self.size = 0

    def __len__(self):
        return self.size

    def __str__(self):
        return self.queue

    def getFront(self):
        if self.isEmpty():
            raise IndexError('The queue is empty.')
        return self.queue[self.front]

    def getRear(self):
        if self.isEmpty():
            raise IndexError('The queue is empty.')
        return self.queue[self.rear]
    
    def enqueue(self, data):
        if self.isFull():
            raise IndexError('The queue is full.')
        self.queue[self.rear] = data
        self.rear = (self.rear + 1) % self.limit
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            raise IndexError('The queue is empty.')
        data = self.queue[self.front]
        self.front = (self.front + 1) % self.limit
        self.size -= 1
        return data

    def isEmpty(self):
        return len(self) == 0

    def isFull(self):
        return len(self) == self.limit
