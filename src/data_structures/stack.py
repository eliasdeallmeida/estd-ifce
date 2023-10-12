class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack:
    def __init__(self, *data):
        self.top = None
        self.size = 0
        if data:
            for element in data:
                self.push(element)

    def __len__(self):
        return self.size

    def __str__(self):
        if self.is_empty():
            return 'The stack is empty.'
        output = 'TOP ['
        node = self.top
        while node:
            output += str(node.data)
            node = node.next
            if node:
                output += ', '
        return output + ']'

    def push(self, data):
        self.top = Node(data, next=self.top)
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError('The stack is empty.')
        deleted_data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return deleted_data

    def peek(self):
        if self.is_empty():
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None
