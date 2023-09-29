from Node import Node


class Stack():
    def __init__(self, data = None):
        self.top = None
        self.size = 0
        if data:
            for element in data:
                self.push(element)
    
    def __str__(self):
        result = ''
        current = self.top
        while current:
            result += str(current.data) + '\n'
            current = current.next
        return result
    
    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node
        self.size += 1
    
    def pop(self):
        if self.isEmpty():
            raise IndexError('The stack is empty.')
        node = self.top.data
        self.top = self.top.next
        self.size -= 1
        return node
    
    def peek(self):
        if self.isEmpty():
            raise IndexError('The stack is empty.')
        return self.top.data
    
    def isEmpty(self):
        return self.top == None
