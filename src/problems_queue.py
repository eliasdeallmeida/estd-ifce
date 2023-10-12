from data_structures.queue import Queue, Node
from data_structures.stack import Stack


# Slide 14
def reverse_queue(queue):
    if queue.is_empty():
        return
    stack = Stack()
    while not queue.is_empty():
        stack.push(queue.dequeue())
    while not stack.is_empty():
        queue.enqueue(stack.pop())


# Slide 14
def reverse_stack(stack):
    if stack.is_empty():
        return
    queue = Queue()
    while not stack.is_empty():
        queue.enqueue(stack.pop())
    while not queue.is_empty():
        stack.push(queue.dequeue())


# Slide 15
def reverse_elements(queue, k):
    stack = Stack()
    for _ in range(k):
        stack.push(queue.dequeue())
    for _ in range(k):
        queue.enqueue(stack.pop())
    for _ in range(queue.size - k):
        queue.enqueue(queue.dequeue())


# Slide 16
class QueueWithTwoStacks():
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def enqueue(self, data):
        self.s1.push(data)

    def dequeue(self):
        if self.s2.is_empty():
            if self.s1.is_empty():
                raise IndexError('The stack is empty.')
            while not self.s1.is_empty():
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
        output = 'FRONT ['
        node = self.front
        while node:
            output += str(node.data)
            node = node.next
            if node:
                output += ', '
        return output + '] REAR'

    def add_front(self, data):
        node = Node(data)
        if self.size == 0:
            self.rear = node
        else:
            self.front.previous = node
            node.next = self.front
        self.front = node
        self.size += 1

    def remove_front(self):
        if self.size == 0:
            raise IndexError('The queue is empty.')
        deleted_data = self.front.data
        self.front = self.front.next
        self.size -= 1
        return deleted_data

    def add_rear(self, data):
        node = Node(data)
        if self.size == 0:
            self.front = node
        else:
            self.rear.next = node
            node.previous = self.rear
        self.rear = node
        self.size += 1

    def remove_rear(self):
        if self.size == 0:
            raise IndexError('The queue is empty.')
        data = self.rear.data
        self.rear = self.rear.previous
        self.rear.next = None
        self.size -= 1
        return data


# Slide 18-19
def reverse_stack_with_queue(stack):
    reverse = Queue()
    node = stack.top
    while node:
        reverse.enqueue(node.data)
        node = node.next
    return reverse


def is_consecutive_pairs(stack):
    result = True
    queue = Queue()
    reverse_stack(stack)
    while not stack.is_empty():
        queue.enqueue(stack.pop())
        if stack.is_empty():
            if queue.size % 2:
                break
            result = False
        queue.enqueue(stack.pop())
        if abs(queue.rear.data - queue.rear.previous.data) != 1:
            result = False
    while not queue.is_empty():
        stack.push(queue.dequeue())
    return result


# Slide 20-21
def reorder_queue(queue):
    pass
