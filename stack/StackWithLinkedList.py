class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


class StackWithLinkedList():
    def __init__(self, *data):
        self.top = None
        self.size = 0
        if data:
            for element in data:
                self.push(element)
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        if self.isEmpty():
            return 'The stack is empty.'
        result = '[TOP] '
        node = self.top
        while node:
            result += str(node.data)
            node = node.next
            if node:
                result += ', '
        return result
    
    def push(self, data):
        self.top = Node(data, self.top)
        self.size += 1
    
    def pop(self):
        if self.isEmpty():
            raise IndexError('The stack is empty.')
        deletedData = self.top.data
        self.top = self.top.next
        self.size -= 1
        return deletedData
    
    def peek(self):
        if self.isEmpty():
            raise IndexError('The stack is empty.')
        return self.top.data
    
    def isEmpty(self):
        return self.top == None and len(self) == 0
