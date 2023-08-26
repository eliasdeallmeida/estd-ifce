from Node import Node

class LinkedList():
    def __init__(self):
        self.head = None
        self.length = 0
    
    def setHead(self, Node):
        self.head = Node
    
    def getHead(self):
        return self.head
    
    def insertAtBeginning(self, data):
        newNode = Node(data)
        if self.length == 0:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1

    def insertAtEnd(self, data):
        newNode = Node(data)
        if self.length == 0:
            self.head = newNode
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = newNode
        self.length += 1
    
    def insertAtGivenPosition(self, position, data):
        if position < 0 or position > self.length:
            return None
        if position == 0:
            self.insertAtBeginning(data)
            return
        if position == self.length:
            self.insertAtEnd(data)
            return
        newNode = Node(data)
        count = 1
        current = self.head
        while count < position - 1:
            count += 1
            current = current.next
        newNode.next = current.next
        current.next = newNode
        self.lenght += 1

    def removeAtBeginning(self):
        if self.length != 0:
            self.head = self.head.next
            self.length -= 1
    
    def removeAtEnd(self):
        if self.length == 0:
            return
        current = self.head
        while current.next != None:
            previous = current
            current = current.next
        previous.next = None
        self.length -= 1
    
    def removeAtGivenPosition(self, position):
        if position < 0 or position > self.length - 1:
            return
        if position == 0:
            self.removeAtBeginning()
            return
        if position == self.length - 1:
            self.removeAtEnd()
            return
        current = self.head.next
        count = 1
        while count != position:
            previous = current
            current = current.next
            count += 1
        previous.next = current.next
        self.length -= 1

    def removeElementsByValue(self, value):
        if self.length == 1 and self.head == value:
            self.head = None
        current = self.head
        count = 0
        while current != None:
            if current.data == value:
                if current.next != None:
                    if count == 0:
                        self.head = current.next
                    else:
                        previous.next = current.next
                else:
                    previous.next = None
                self.length -= 1
            count += 1
            previous = current
            current = current.next

    def printElements(self):
        position = 0
        current = self.head
        while current != None:
            print(f'{position} - {current.data}')
            position += 1
            current = current.next
