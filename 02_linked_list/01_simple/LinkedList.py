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
            while current.next:
                current = current.next
            current.next = newNode
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
        newNode = Node(data)
        count = 1
        current = self.head
        while count != position:
            current = current.next
            count += 1
        newNode.next = current.next
        current.next = newNode
        self.length += 1

    def removeAtBeginning(self):
        if self.length:
            self.head = self.head.next
            self.length -= 1
    
    def removeAtEnd(self):
        if self.length == 0:
            return
        current = self.head
        while current.next:
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
        current = self.head
        previous = None
        while current:
            if current.data == value:
                if previous == None:
                    self.head = current.next
                else:
                    previous.next = current.next
                self.length -= 1
            else:
                previous = current
            current = current.next
    
    def removeRepetitions(self):
        current = self.head
        while current.next:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next
    
    def reverseInPairs(self):
        current = self.head
        while current and current.next:
            currentCopy = current.data
            current.data = current.next.data
            current.next.data = currentCopy
            current = current.next.next

    def reverse(self):
        if self.length == 1:
            return
        current = self.head
        previous = None
        while current.next:
            next = current.next
            current.next = previous
            previous = current
            current = next
        current.next = previous
        self.head = current
    
    def reverseAtGivenElement(self, current):
        reverseList = LinkedList()
        while current:
            reverseList.insertAtBeginning(current.data)
            current = current.next
        return reverseList.head

    def isPalindrome(self):
        if self.head == None:
            return False
        if self.length == 1:
            return True
        current = firstHalf = self.head
        for _ in range(self.length // 2):
            current = current.next
        if self.length % 2:
            secondHalf = self.reverseAtGivenElement(current.next)
        else:
            secondHalf = self.reverseAtGivenElement(current)
        while secondHalf:
            if firstHalf.data != secondHalf.data:
                return False
            firstHalf = firstHalf.next
            secondHalf = secondHalf.next
        return True

    def printElements(self):
        position = 0
        current = self.head
        while position != self.length:
            print(f'{position} - {current.data}')
            position += 1
            current = current.next
