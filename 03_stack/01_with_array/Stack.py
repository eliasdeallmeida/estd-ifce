class Stack():
    def __init__(self, capacity = 1):
        self.top = 1
        self.capacity = capacity
        self.a = [None] * capacity
    
    def push(self, data):
        if self.capacity == self.top + 1:
            print('Stack Overflow')
            return
        self.top += 1
        self.a[self.top] = data
    
    def pop(self):
        if self.top == -1:
            print('Stack Underflow')
            return
        temp = temp.a[self.top]
        self.top -= 1
        return temp
    
    def peek(self):
        if self.top == -1:
            print('Stack Overflow')
            return
        return self.a[self.top]
    
    def isEmpty(self):
        return self.top == -1
    
    def isFull(self):
        return self.capacity == self.top + 1
