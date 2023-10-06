class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


class LinkedList():
    def __init__(self):
        self.head = None
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        if self.isEmpty():
            return
        result = '['
        node = self.head
        for _ in range(self.size):
            result += str(node.data)
            if node.next:
                result += ' -> '
            node = node.next
        return result + ']'
    
    def insertAtBeginning(self, data):
        if self.isEmpty():
            self.head = Node(data)
        else:
            self.head = Node(data, self.head)
        self.size += 1

    def insertAtEnd(self, data):
        if self.isEmpty():
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)
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
            node.next = Node(data, node.next)
            self.size += 1

    def removeAtBeginning(self):
        if self.isEmpty():
            raise IndexError('The linked list is empty.')
        self.head = self.head.next
        self.size -= 1
    
    def removeAtEnd(self):
        if self.isEmpty():
            raise IndexError('The linked list is empty.')
        current = self.head
        while current.next:
            previous = current
            current = current.next
        previous.next = None
        self.size -= 1
    
    def removeAtGivenIndex(self, index):
        if index < 0 or index > len(self) - 1:
            raise IndexError('Invalid index given')
        if index == 0:
            self.removeAtBeginning()
        elif index == len(self) - 1:
            self.removeAtEnd()
        else:
            current = self.head.next
            for _ in range(index - 1):
                previous = current
                current = current.next
            previous.next = current.next
            self.size -= 1
    
    def isEmpty(self):
        return self.head == None and len(self) == 0
