from Queue import Queue
from Stack import *


def reverseQueue(queue):
    if queue.isEmpty():
        return
    stack = Stack()
    while not queue.isEmpty():
        stack.push(queue.dequeue())
    while not stack.isEmpty():
        queue.enqueue(stack.pop())


def reverseStack(stack):
    if stack.isEmpty():
        return
    queue = Queue()
    while not stack.isEmpty():
        queue.enqueue(stack.pop())
    while not queue.isEmpty():
        stack.push(queue.dequeue())


def reverseQueueByK(queue, k):
    if k <= 1:
        return
    pass
