class Stack():
    def __init__(self, data = None):
        self.top = None
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
    
    def pop(self):
        if self.isEmpty():
            raise IndexError('The stack is empty.')
        node = self.top.data
        self.top = self.top.next
        return node
    
    def peek(self):
        if self.isEmpty():
            raise IndexError('The stack is empty.')
        return self.top.data
    
    def isEmpty(self):
        return self.top == None


class Node():
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
    
    def setData(self, data):
        self.data = data
    
    def getData(self):
        return self.data
    
    def setNext(self, next):
        self.next = next
    
    def getNext(self):
        return self.next
    
    def hasNext(self):
        return self.next != None
