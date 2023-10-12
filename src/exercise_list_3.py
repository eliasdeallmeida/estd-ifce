from data_structures.stack import Stack
from data_structures.queue import Queue


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
    while not d.is_empty():
        q.enqueue(d.remove_first())
    return q


# Q5
class QueueQ5():
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def __str__(self):
        output = ''
        self.transfer(self.s1, self.s2)
        node = self.s2.top
        while node:
            output += str(node.data) + ' -> '
            node = node.next
        self.transfer(self.s2, self.s1)
        return output

    def enqueue(self, data):
        self.transfer(self.s2, self.s1)
        self.s1.push(data)

    def dequeue(self):
        if self.is_empty():
            return
        self.transfer(self.s1, self.s2)
        return self.s2.pop()

    def is_empty(self):
        return self.s1.is_empty() and self.s2.is_empty()

    def front(self):
        if self.is_empty():
            return
        self.transfer(self.s1, self.s2)
        return self.s2.peek()

    def rear(self):
        if self.is_empty():
            return
        self.transfer(self.s2, self.s1)
        return self.s1.peek()

    def transfer(self, origin, destiny):
        while not origin.is_empty():
            destiny.push(origin.pop())


# Q6
class DequeQ6():
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def __str__(self):
        output = ''
        self.transfer(self.s1, self.s2)
        node = self.s2.top
        while node:
            output += str(node.data) + ' -> '
            node = node.next
        self.transfer(self.s2, self.s1)
        return output

    def add_front(self, data):
        self.transfer(self.s1, self.s2)
        self.s2.push(data)

    def remove_front(self):
        if self.is_empty():
            return
        self.transfer(self.s1, self.s2)
        return self.s2.pop()

    def add_rear(self, data):
        self.transfer(self.s2, self.s1)
        self.s1.push(data)

    def remove_rear(self):
        if self.is_empty():
            return
        self.transfer(self.s2, self.s1)
        return self.s1.pop()

    def is_empty(self):
        return self.s1.is_empty() and self.s2.is_empty()

    def get_front(self):
        if self.is_empty():
            return
        self.transfer(self.s1, self.s2)
        return self.s2.peek()

    def get_rear(self):
        if self.is_empty():
            return
        self.transfer(self.s2, self.s1)
        return self.s1.peek()

    def transfer(self, origin, destiny):
        while not origin.is_empty():
            destiny.push(origin.pop())


# Q7
class StackQ7():
    def __init__(self):
        self.q = Queue()

    def __str__(self):
        if self.isEmpty():
            return 'The stack is empty.'
        output = ''
        node = self.q.front
        while node:
            output += str(node.data)
            node = node.next
            if node:
                output += ', '
        return output + ' [TOP]'

    def push(self, data):
        self.q.enqueue(data)

    def pop(self):
        if self.q.is_empty():
            return
        for _ in range(self.q.size - 1):
            self.q.enqueue(self.q.dequeue())
        return self.q.dequeue()

    def peek(self):
        return self.q.rear.data

    def is_empty(self):
        return self.q.is_empty()


# Q8
def reverse_first_k_elements(queue, k):
    stack = Stack()
    for _ in range(k):
        stack.push(queue.dequeue())
    for _ in range(k):
        queue.enqueue(stack.pop())
    for _ in range(len(queue) - k):
        queue.enqueue(queue.dequeue())
