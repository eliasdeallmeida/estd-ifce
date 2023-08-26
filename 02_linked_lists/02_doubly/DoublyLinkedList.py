from Node import Node

class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def setHead(self, head):
        self.head = head
    
    def getHead(self):
        return self.head
    
    def setTail(self, tail):
        self.head = tail
    
    def getTail(self):
        return self.tail
    
    def insertAtBeginning(self, data):
        newNode = Node(data)
        if self.length == 0:
            self.head = self.tail = newNode
        else:
            newNode.next = self.head
            self.head.previous = self.head = newNode
        self.length += 1
    
    def insertAtEnd(self, data):
        newNode = Node(data)
        if self.length == 0:
            self.head = self.tail = newNode
        else:
            newNode.previous = self.tail
            self.tail.next = self.tail = newNode
        self.length += 1

    def insertAtGivenPosition(self, position, data):
        if position < 0 or position > self.length:
            return
        if position == 0:
            self.insertAtBeginning(data)
            return
        if position == self.length:
            self.insertAtEnd(data)
            return
        current = self.head
        count = 1
        while count != position:
            current = current.next
            count += 1
        newNode = Node(data)
        newNode.next = current
        newNode.previous = current.previous
        current.previous.next = current.previous = newNode
        self.length += 1
    
    def removeAtBeginning(self):
        if self.length:
            self.head = self.head.next
            self.head.previous = None
            self.length -= 1
    
    def removeAtEnd(self):
        if self.length:
            self.tail = self.tail.previous
            self.tail.next = None
            self.length -= 1
    
    def removeAtGivenPosition(self, position):
        if position < 0 or position >= self.length:
            return
        if position == 0:
            self.removeAtBeginning()
            return
        if position == self.length - 1:
            self.removeAtEnd()
            return
        current = self.head
        count = 1
        while count != position:
            current = current.next
            count += 1
        current.previous.next = current.next
        current.next.previous = current.previous
        self.length -= 1
    
    def printElements(self):
        position = 0
        current = self.head
        while current:
            print(f'{position} - {current.data}')
            position += 1
            current = current.next
