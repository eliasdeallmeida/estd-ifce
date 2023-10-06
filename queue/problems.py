import os
import sys


sys.path.append(os.path.dirname(os.path.dirname(__file__)))


from QueueWithLinkedList import *
from stack.StackWithLinkedList import *


# Slide 14
def reverseQueue(queue):
    if queue.isEmpty():
        return
    stack = StackWithLinkedList()
    while not queue.isEmpty():
        stack.push(queue.dequeue())
    while not stack.isEmpty():
        queue.enqueue(stack.pop())


# Slide 14
def reverseStack(stack):
    if stack.isEmpty():
        return
    queue = QueueWithLinkedList()
    while not stack.isEmpty():
        queue.enqueue(stack.pop())
    while not queue.isEmpty():
        stack.push(queue.dequeue())


# Slide 15
def reverseElements(queue, k):
    stack = StackWithLinkedList()
    for _ in range(k):
        stack.push(queue.dequeue())
    for _ in range(k):
        queue.enqueue(stack.pop())
    for _ in range(queue.size - k):
        queue.enqueue(queue.dequeue())


# Slide 16
class QueueWithTwoStacks():
    def __init__(self):
        self.s1 = StackWithLinkedList()
        self.s2 = StackWithLinkedList()
    
    def enqueue(self, data):
        self.s1.push(data)
    
    def dequeue(self):
        if self.s2.isEmpty():
            if self.s1.isEmpty():
                raise IndexError('The stack is empty.')
            while not self.s1.isEmpty():
                self.s2.push(self.s1.pop())
            return self.s2.pop()
        else:
            return self.s2.pop()


# Slide 17
class Deque():
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        if self.size == 0:
            return 'The queue is empty.'
        result = ''
        element = self.front
        while element:
            result += str(element.data)
            if element.next:
                result += ' -> '
            element = element.next
        return result

    def addFront(self, data):
        node = Node(data)
        if self.size == 0:
            self.rear = node
        else:
            self.front.previous = node
            node.next = self.front
        self.front = node
        self.size += 1

    def removeFront(self):
        if self.size == 0:
            raise IndexError('The queue is empty.')
        data = self.front.data
        self.front = self.front.next
        self.size -= 1
        return data

    def addRear(self, data):
        node = Node(data)
        if self.size == 0:
            self.front = node
        else:
            self.rear.next = node
            node.previous = self.rear
        self.rear = node
        self.size += 1

    def removeRear(self):
        if self.size == 0:
            raise IndexError('The queue is empty.')
        data = self.rear.data
        self.rear = self.rear.previous
        self.rear.next = None
        self.size -= 1
        return data


# Slide 18-19
def reverseStackWithQueue(stack):
    reverse = QueueWithLinkedList()
    element = stack.top
    while element:
        reverse.enqueue(element.data)
        element = element.next
    return reverse


def isConsecutivePairs(stack):
    result = True
    queue = QueueWithLinkedList()
    reverseStack(stack)
    while not stack.isEmpty():
        queue.enqueue(stack.pop())
        if stack.isEmpty():
            if queue.size % 2:
                break
            result = False
        queue.enqueue(stack.pop())
        if abs(queue.rear.data - queue.rear.previous.data) != 1:
            result = False
    while not queue.isEmpty():
        stack.push(queue.dequeue())
    return result


# Slide 20-21
def reorderQueue(queue):
    pass
