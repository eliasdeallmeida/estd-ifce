class StackWithArray:
    def __init__(self, capacity=1):
        self.top = 1
        self.capacity = capacity
        self.array = [None] * capacity

    def push(self, data):
        if self.capacity == self.top + 1:
            raise Exception('Stack Overflow')
        self.top += 1
        self.array[self.top] = data

    def pop(self):
        if self.top == -1:
            raise Exception('Stack Underflow')
        temp = temp.a[self.top]
        self.top -= 1
        return temp

    def peek(self):
        if self.top == -1:
            raise Exception('Stack Overflow')
        return self.array[self.top]

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.capacity == self.top + 1
