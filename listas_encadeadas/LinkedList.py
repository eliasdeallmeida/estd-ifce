from Node import Node

class LinkedList():
    def __init__(self):
        self.length = 0
        self.head = None
    
    def setHead(self, Node):
        self. length += 1
        self.head = Node
    
    def getHead(self):
        return self.head
    
    def insertAtBeggining(self, data):
        newNode = Node()
        newNode.data = data
        if self.length == 0:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1

    def insertAtEnd(self, data):
        newNode = Node()
        newNode.data = data
        if self.length == 0:
            self.head = newNode
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = newNode
        self.length += 1
    
    def insertAtGivenPosition(self, position, data):
        if position > self.length or position < 0:
            return None
        if position == 0:
            self.insertAtBeggining(data)
            return
        if position == self.length:
            self.insertAtEnd(data)
            return
        newNode = Node()
        newNode.data = data
        count = 1
        current = self.head
        while count < position - 1:
            count += 1
            current = current.next
        newNode.next = current.next
        current.next = newNode
        self.lenght += 1
