from Node import Node


class Queue():
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
    
    def __str__(self):
        if self.size == 0:
            return 'The queue is empty.'
        result = ''
        element = self.front
        while element:
            result += str(element.data)
            if element.next:
                result += ' -> '
            element = element.next
        return result
    
    def __len__(self):
        return self.size
    
    def getFront(self):
        return self.front.data
    
    def getRear(self):
        return self.rear.data
    
    def enqueue(self, data):
        node = Node(data)
        if self.size == 0:
            self.front = node
        else:
            self.rear.next = node
            node.previous = self.rear
        self.rear = node
        self.size += 1
    
    def dequeue(self):
        if self.size > 0:
            data = self.front.data
            self.front = self.front.next
            self.size -= 1
            return data
        raise IndexError('The queue is empty.')
    
    def isEmpty(self):
        return self.front == None
