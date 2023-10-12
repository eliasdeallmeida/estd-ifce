class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class SimplyLinkedList:
    def __init__(self, *data):
        self.head = None
        self.size = 0
        if data:
            for element in data:
                self.insert_at_end(element)

    def __len__(self):
        return self.size

    def __str__(self):
        if self.is_empty():
            return 'The simply linked list is empty.'
        output = 'HEAD ['
        node = self.head
        while node:
            output += str(node.data)
            node = node.next
            if node:
                output += ', '
        return output + ']'

    def insert_at_beginning(self, data):
        if self.is_empty():
            self.head = Node(data)
        else:
            self.head = Node(data, next=self.head)
        self.size += 1

    def insert_at_end(self, data):
        if self.is_empty():
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)
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
            node.next = Node(data, next=node.next)
            self.size += 1

    def remove_at_beginning(self):
        if self.is_empty():
            raise IndexError('The simply linked list is empty.')
        self.head = self.head.next
        self.size -= 1

    def remove_at_end(self):
        if self.is_empty():
            raise IndexError('The simply linked list is empty.')
        if self.size == 1:
            self.head = None
        else:
            node = self.head
            while node.next:
                previous_node = node
                node = node.next
            previous_node.next = None
        self.size -= 1

    def remove_at_index(self, index):
        if index < 0 or index > self.size - 1:
            raise IndexError('Invalid index given')
        if index == 0:
            self.remove_at_beginning()
        elif index == self.size - 1:
            self.remove_at_end()
        else:
            node = self.head
            for _ in range(index):
                previous_node = node
                node = node.next
            previous_node.next = node.next
            self.size -= 1

    def is_empty(self):
        return self.head is None
