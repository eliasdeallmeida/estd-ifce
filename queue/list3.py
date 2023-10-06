import os
import sys


sys.path.append(os.path.dirname(os.path.dirname(__file__)))


from QueueWithLinkedList import *
from stack.StackWithLinkedList import *


# Q1
# a) 5, 3, 2, 8
# b) 7, 3, 5, 9, 19
# c) 71, 31, 9, 11, 1


# Q2
# tam = 32 - (15 - 5)
# tam = 32 - 10
# tam = 22
# Logo, no final das operações, a fila terá seu tamanho igual a 22


# Q3
# a) 9, 5, 9, 4, 10, 4
# b) 5, 4, 5, 10, 9, 6
# c) 5, 5, 4, 9, 10, 6


# Q4
def transfer(d, q):
    while not d.isEmpty():
        q.enqueue(d.removeFront())
    return q


# Q5
class QueueQ5():
    def __init__(self):
        self.s1 = StackWithLinkedList()
        self.s2 = StackWithLinkedList()
    
    def __str__(self):
        result = ''
        self.transfer(self.s1, self.s2)
        pointer = self.s2.top
        while pointer:
            result += str(pointer.data) + ' -> '
            pointer = pointer.next
        self.transfer(self.s2, self.s1)
        return result
    
    def enqueue(self, data):
        self.transfer(self.s2, self.s1)
        self.s1.push(data)

    def dequeue(self):
        if self.isEmpty():
            return
        self.transfer(self.s1, self.s2)
        return self.s2.pop()
    
    def isEmpty(self):
        return self.s1.isEmpty() and self.s2.isEmpty()
    
    def front(self):
        if self.isEmpty():
            return
        self.transfer(self.s1, self.s2)
        return self.s2.peek()
    
    def rear(self):
        if self.isEmpty():
            return
        self.transfer(self.s2, self.s1)
        return self.s1.peek()
    
    def transfer(self, origin, destiny):
        while not origin.isEmpty():
            destiny.push(origin.pop())


# Q6
class DequeQ6():
    def __init__(self):
        self.s1 = StackWithLinkedList()
        self.s2 = StackWithLinkedList()

    def __str__(self):
        result = ''
        self.transfer(self.s1, self.s2)
        pointer = self.s2.top
        while pointer:
            result += str(pointer.data) + ' -> '
            pointer = pointer.next
        self.transfer(self.s2, self.s1)
        return result

    def addFront(self, data):
        self.transfer(self.s1, self.s2)
        self.s2.push(data)

    def removeFront(self):
        if self.isEmpty():
            return
        self.transfer(self.s1, self.s2)
        return self.s2.pop()

    def addRear(self, data):
        self.transfer(self.s2, self.s1)
        self.s1.push(data)

    def removeRear(self):
        if self.isEmpty():
            return
        self.transfer(self.s2, self.s1)
        return self.s1.pop()
    
    def isEmpty(self):
        return self.s1.isEmpty() and self.s2.isEmpty()

    def front(self):
        if self.isEmpty():
            return
        self.transfer(self.s1, self.s2)
        return self.s2.peek()

    def rear(self):
        if self.isEmpty():
            return
        self.transfer(self.s2, self.s1)
        return self.s1.peek()
    
    def transfer(self, origin, destiny):
        while not origin.isEmpty():
            destiny.push(origin.pop())


# Q7
class StackQ7():
    def __init__(self):
        self.q = QueueWithLinkedList()
    
    def __str__(self):
        result = ''
        for _ in range(self.q.size - 1):
            self.q.enqueue(self.q.dequeue())
        node = self.q.front
        while node:
            result += str(node.data) + '\n'
            node = node.previous
        self.q.enqueue(self.q.dequeue())
        return result
    
    def push(self, data):
        self.q.enqueue(data)

    def pop(self):
        if self.q.isEmpty():
            return
        if self.q.size > 1:
            for _ in range(self.q.size - 1):
                self.q.enqueue(self.q.dequeue())
            self.q.front.next.previous = None
        else:
            self.q.rear = None
        return self.q.dequeue()

    def peek(self):
        return self.q.rear.data
    
    def isEmpty(self):
        return self.q.isEmpty()


# Q8
def reverseFirstKElements(queue, k):
    stack = StackWithLinkedList()
    for _ in range(k):
        stack.push(queue.dequeue())
    for _ in range(k):
        queue.enqueue(stack.pop())
    for _ in range(len(queue) - k):
        queue.enqueue(queue.dequeue())
