class Node():
    def __init__(self, data, previous = None, next = None):
        self.data = data
        self.previous = previous
        self.next = next


class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        if self.isEmpty():
            return
        result = '['
        node = self.head
        while node:
            result += str(node.data)
            if node.next:
                result += ' -> '
            node = node.next
        return result + ']'

    def insertAtBeginning(self, data):
        if self.isEmpty():
            self.head = self.tail = Node(data)
        else:
            self.head.previous = self.head = Node(data, None, self.head)
        self.size += 1
    
    def insertAtEnd(self, data):
        if self.isEmpty():
            self.head = self.tail = Node(data)
        else:
            self.tail.next = self.tail = Node(data, self.tail, None)
        self.size += 1

    def insertAtGivenIndex(self, data, index):
        if index < 0 or index > len(self):
            raise IndexError('Invalid index given.')
        if index == 0:
            self.insertAtBeginning(data)
        elif index == len(self):
            self.insertAtEnd(data)
        else:
            node = self.head
            for _ in range(index - 1):
                node = node.next
            node.next = node.next.previous = Node(data, node, node.next)
            self.size += 1
    
    def removeAtBeginning(self):
        if self.isEmpty():
            raise IndexError('The doubly linked list is empty.')
        self.head = self.head.next
        self.head.previous = None
        self.size -= 1
    
    def removeAtEnd(self):
        if self.isEmpty():
            raise IndexError('The doubly linked list is empty.')
        self.tail = self.tail.previous
        self.tail.next = None
        self.size -= 1
    
    def removeAtGivenIndex(self, index):
        if index < 0 or index >= len(self):
            raise IndexError('Invalid index given')
        if index == 0:
            self.removeAtBeginning()
        elif index == len(self) - 1:
            self.removeAtEnd()
        else:
            node = self.head
            for _ in range(index - 1):
                node = node.next
            node.previous.next = node.next
            node.next.previous = node.previous
            self.size -= 1
    
    def isEmpty(self):
        return self.head == self.tail == None and len(self) == 0
