class Node:
    def __init__(self, data, previous=None, next=None):
        self.data = data
        self.previous = previous
        self.next = next


class Queue:
    def __init__(self, *data):
        self.front = None
        self.rear = None
        self.size = 0
        if data:
            for element in data:
                self.enqueue(element)

    def __len__(self):
        return self.size

    def __str__(self):
        if self.is_empty():
            return 'The queue is empty.'
        output = 'FRONT ['
        node = self.front
        while node:
            output += str(node.data)
            if node.next:
                output += ', '
            node = node.next
        return output + '] REAR'

    def enqueue(self, data):
        if self.is_empty():
            self.front = self.rear = Node(data)
        else:
            self.rear.next = self.rear = Node(data, previous=self.rear)
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError('The queue is empty.')
        deleted_data = self.front.data
        self.front = self.front.next
        self.size -= 1
        if self.size == 0:
            self.rear = None
        return deleted_data

    def get_front(self):
        if self.is_empty():
            return None
        return self.front.data

    def get_rear(self):
        if self.is_empty():
            return None
        return self.rear.data

    def is_empty(self):
        return self.front is None and self.rear is None
