from Stack import *
from Queue import Queue


# Q4
def transferir(d, q):
    while not d.isEmpty():
        q.enqueue(d.removeFront())
    return q


# Q5
class QueueQ5():
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()
    
    def __str__(self):
        result = ''
        self.transfer(self.s1, self.s2)
        pointer = self.s2.top
        while pointer:
            result += str(pointer.data) + ' -> '
            pointer = pointer.next
        self.transfer(self.s2, self.s1)
        return result
    
    def transfer(self, origin, destiny):
        while not origin.isEmpty():
            destiny.push(origin.pop())

    def enqueue(self, data):
        self.s1.push(data)

    def dequeue(self):
        if self.s1.isEmpty():
            return
        self.transfer(self.s1, self.s2)
        data = self.s2.pop()
        self.transfer(self.s2, self.s1)
        return data


# Q6
class DequeQ6():
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def __str__(self):
        result = ''
        self.transfer(self.s1, self.s2)
        pointer = self.s2.top
        while pointer:
            result += str(pointer.data) + ' -> '
            pointer = pointer.next
        self.transfer(self.s2, self.s1)
        return result
    
    def transfer(self, origin, destiny):
        while not origin.isEmpty():
            destiny.push(origin.pop())
    
    def addFront(self, data):
        if self.s1.isEmpty():
            self.addRear(data)
        else:
            self.transfer(self.s1, self.s2)
            self.s1.push(data)
            self.transfer(self.s2, self.s1)

    def removeFront(self):
        if self.s1.isEmpty():
            return
        self.transfer(self.s1, self.s2)
        data = self.s2.pop()
        self.transfer(self.s2, self.s1)
        return data

    def addRear(self, data):
        self.s1.push(data)

    def removeRear(self):
        if self.s1.isEmpty():
            return
        return self.s1.pop()


# Q7
class StackQ7():
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def __str__(self) -> str:
        result = ''
        pointer = self.q1.front
        while pointer:
            result += str(pointer.data) + ' <- '
            pointer = pointer.next
        result += 'Topo'
        return result
    
    def transfer(self, origin, destiny, size):
        while origin.size != size:
            destiny.enqueue(origin.dequeue())
    
    def push(self, data):
        self.q1.enqueue(data)

    def pop(self):
        if self.q1.isEmpty():
            return
        self.transfer(self.q1, self.q2, 1)
        data = self.q1.dequeue()
        self.transfer(self.q2, self.q1, 0)
        return data

    def peek(self):
        return self.q1.getFront()


# Q8
def inverterFila(fila, k):
    pilha = Stack()
    for _ in range(k):
        pilha.push(fila.dequeue())
    for _ in range(k):
        fila.enqueue(pilha.pop())
    for _ in range(fila.size - k):
        fila.enqueue(fila.dequeue())
