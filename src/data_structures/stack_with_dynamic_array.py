class StackWithDynamicArray:
    def __init__(self, capacity=1):
        self.top = 1
        self.capacity = capacity
        self.array = [None] * capacity

    def push(self, data):
        if self.capacity == self.top + 1:
            self.resize(1)
        self.top += 1
        self.array[self.top] = data

    def pop(self):
        if self.top == -1:
            raise Exception('Stack Overflow')
        if self.top < self.capacity // 2:
            self.resize(0)
        temp = self.array[self.top]
        self.top -= 1
        return temp

    def resize(self, dir):
        if dir == 1:
            self.capacity = self.capacity * 2
        else:
            self.capacity = self.capacity // 2
        new_array = [None] * self.capacity
        for i in range(self.top + 1):
            new_array[i] = self.array[i]
        self.array = new_array
