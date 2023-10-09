class Node():
    def __init__(self, data, previous = None, next = None):
        self.data = data
        self.previous = previous
        self.next = next


class QueueWithLinkedList():
    def __init__(self, *data):
        self.front = None
        self.rear = None
        self.size = 0
        if data:
            for element in data:
                self.enqueue(element)
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        if self.isEmpty():
            return 'The queue is empty.'
        result = '[FRONT] '
        node = self.front
        while node:
            result += str(node.data)
            if node.next:
                result += ', '
            node = node.next
        return result + ' [REAR]'
    
    def enqueue(self, data):
        if self.isEmpty():
            self.front = self.rear = Node(data)
        else:
            self.rear.next = self.rear = Node(data, self.rear, None)
        self.size += 1
    
    def dequeue(self):
        if self.isEmpty():
            raise IndexError('The queue is empty.')
        deletedData = self.front.data
        self.front = self.front.next
        self.size -= 1
        if len(self) == 0:
            self.rear = None
        return deletedData

    def isEmpty(self):
        return self.front == self.rear == None and len(self) == 0
