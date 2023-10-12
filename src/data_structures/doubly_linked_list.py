class Node:
    def __init__(self, data, previous=None, next=None):
        self.data = data
        self.previous = previous
        self.next = next


class DoublyLinkedList:
    def __init__(self, *data):
        self.head = None
        self.tail = None
        self.size = 0
        if data:
            for element in data:
                self.insert_at_end(element)

    def __len__(self):
        return self.size

    def __str__(self):
        if self.is_empty():
            return 'The doubly linked list is empty.'
        output = 'HEAD ['
        node = self.head
        while node:
            output += str(node.data)
            node = node.next
            if node:
                output += ', '
        return output + '] TAIL'

    def insert_at_beginning(self, data):
        if self.is_empty():
            self.head = self.tail = Node(data)
        else:
            self.head.previous = self.head = Node(data, next=self.head)
        self.size += 1

    def insert_at_end(self, data):
        if self.is_empty():
            self.head = self.tail = Node(data)
        else:
            self.tail.next = self.tail = Node(data, previous=self.tail)
        self.size += 1

    def insert_at_index(self, data, index):
        if index < 0 or index > self.size:
            raise IndexError('Invalid index given.')
        if index == 0:
            self.insert_at_beginning(data)
        elif index == self.size:
            self.insert_at_end(data)
        else:
            node = self.head
            for _ in range(index - 1):
                node = node.next
            node.next = node.next.previous = Node(data, node, node.next)
            self.size += 1

    def remove_at_beginning(self):
        if self.is_empty():
            raise IndexError('The doubly linked list is empty.')
        if self.size == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.previous = None
        self.size -= 1

    def remove_at_end(self):
        if self.is_empty():
            raise IndexError('The doubly linked list is empty.')
        if self.size == 1:
            self.head = self.tail = None
        else:
            self.tail = self.tail.previous
            self.tail.next = None
        self.size -= 1

    def remove_at_index(self, index):
        if index < 0 or index >= self.size:
            raise IndexError('Invalid index given')
        if index == 0:
            self.remove_at_beginning()
        elif index == self.size - 1:
            self.remove_at_end()
        else:
            node = self.head.next
            for _ in range(index - 1):
                node = node.next
            node.previous.next = node.next
            node.next.previous = node.previous
            self.size -= 1

    def is_empty(self):
        return self.head is None and self.tail is None
