import os
import sys


sys.path.append(os.path.dirname(os.path.dirname(__file__)))


from QueueWithLinkedList import *
from stack.StackWithLinkedList import *


# Q1
# a)
#    fila: 5        |
#    fila: 5, 3     |
#    fila: 3		|   retorna 5
#    fila: 3, 2     |
#    fila: 3, 2, 8  |
#    fila: 2, 8		|   retorna 3
#    fila: 8 		|   retorna 2
#    fila: 8, 9     |
#    fila: 8, 9, 1  |
#    fila: 9, 1		|   retorna 8
#    fila: 9, 1, 7  |

# b)
#    fila: 7        |
#    fila: 7, 3     |
#    fila: 3		|   retorna 7
#    fila: 3, 5     |
#    fila: 3, 5, 9  |
#    fila: 5, 9		|   retorna 3
#    fila: 9		|   retorna 5
#    fila: 9, 19    |
#    fila: 9, 19, 1 |
#    fila: 19, 1	|	retorna 9
#    fila: 1		|   retorna 19

# c)
#    fila: 71       |
#    fila: 71, 31   |
#    fila: 31		|   retorna 71
#    fila: 			|   retorna 31
#    fila: 9        |
#    fila: 9, 11    |
#    fila: 11		|   retorna 9
#    fila: 			|   retorna 11
#    fila: 1        |
#    fila: 1, 20    |
#    fila: 20		|   retorna 1


# Q2
# tam = 32 - (15 - 5)
# tam = 32 - 10
# tam = 22
# Logo, no final das operações, a fila terá seu tamanho igual a 22


# Q3
# a)
#    deque: 4               |
#    deque: 4, 8            |
#    deque: 4, 8, 9         |
#    deque: 5, 4, 8, 9      |
#    deque: 5, 4, 8, 9	    |	retorna 9
#    deque: 4, 8, 9		    |   retorna 5
#    deque: 4, 8		    |	retorna 9
#    deque: 4, 8, 10        |
#    deque: 4, 8, 10	    |	retorna 4
#    deque: 4, 8, 10	    |	retorna 10
#    deque: 4, 8, 10, 6	    |	retorna 6
#    deque: 8, 10, 6	    |	retorna 4

# b)
#    deque: 4               |
#    deque: 4, 8            |
#    deque: 4, 8, 9         |
#    deque: 4, 8, 9, 5      |
#    deque: 4, 8, 9, 5		|	retorna 5
#    deque: 8, 9, 5			|   retorna 4
#    deque: 8, 9			|	retorna 5
#    deque: 10, 8, 9        |
#    deque: 10, 8, 9		|	retorna 10
#    deque: 10, 8, 9		|	retorna 9
#    deque: 6, 10, 8, 9	    |
#    deque: 6, 10, 8, 9, 10 |
#    deque: 10, 8, 9, 10	|   retorna 6

# c)
#    deque: 4               |
#    deque: 8, 4            |
#    deque: 9, 8, 4         |
#    deque: 9, 8, 4, 5      |
#    deque: 9, 8, 4, 5		|	retorna 5
#    deque: 9, 8, 4			|   retorna 5
#    deque: 9, 8			|	retorna 4
#    deque: 9, 8, 10        |
#    deque: 9, 8, 10		|	retorna 9
#    deque: 9, 8, 10		|	retorna 10
#    deque: 6, 9, 8, 10     |
#    deque: 6, 9, 8, 10, 10 |
#    deque: 9, 8, 10, 10	|	retorna 6


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
        if self.isEmpty():
            return 'The stack is empty.'
        result = ''
        node = self.q.front
        while node:
            result += str(node.data)
            node = node.next
            if node:
                result += ', '
        return result + ' [TOP]'
    
    def push(self, data):
        self.q.enqueue(data)

    def pop(self):
        if self.q.isEmpty():
            return
        for _ in range(self.q.size - 1):
            self.q.enqueue(self.q.dequeue())
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
