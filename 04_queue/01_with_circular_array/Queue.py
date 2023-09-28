class Queue():
    def __init__(self, limit = 5):
        self.queue = [None] * limit
        self.limit = limit
        self.front = 0
        self.rear = 0
        self.size = 0

    def __str__(self):
        return self.queue

    def __len__(self):
        return self.size

    def getFront(self):
        if self.size > 0:
            return self.queue[self.front]
        raise IndexError('The queue is empty.')

    def getRear(self):
        if self.size > 0:
            return self.queue[self.rear]
        raise IndexError('The queue is empty.')
    
    def enqueue(self, data):
        if self.isFull():
            return
        self.queue[self.rear] = data
        self.rear = (self.rear + 1) % self.limit
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            return
        data = self.queue[self.front]
        self.front = (self.front + 1) % self.limit
        self.size -= 1
        return data

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.limit
