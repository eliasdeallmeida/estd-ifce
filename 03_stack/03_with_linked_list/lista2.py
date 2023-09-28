from Stack import Stack


# Q3
def transfer(s, t):
    while s.top != None:
        t.push(s.pop())


# Q4
def empty(stack):
    if stack.isEmpty():
        return
    stack.pop()
    empty(stack)


# Q5
def reverseArray(array):
    stack = Stack()
    reverse = []
    for element in array:
        stack.push(element)
    for _ in range(len(array)):
        reverse.append(stack.pop())
    return reverse


# Q6
class StackQ6():
    def __init__(self, n):
        self.n = n
        self.a = [None] * n
        self.a[0] = 0
    
    def push(self, data):
        if self.a[0] == self.n - 1:
            return
        self.a[0] += 1
        self.a[self.a[0]] = data

    def pop(self):
        if self.isEmpty():
            return
        data = self.a[self.a[0]]
        self.a[self.a[0]] = None
        self.a[0] -= 1
        return data

    def peek(self):
        return self.a[self.a[0]]

    def isEmpty(self):
        return self.a[0] == 0
    
    def isFull(self):
        return self.a[0] == self.n - 1
    
    def empty(self):
        self.a = [None] * self.n
        self.a[0] = 0


# Q7 V1
class P1():
    def __init__(self, a, n):
        self.t1 = -1
        self.limit = n // 2
        self.a = a
    
    def push(self, data):
        if self.t1 + 1 == self.limit:
            return
        self.t1 += 1
        self.a[self.t1] = data
    
    def pop(self):
        if self.t1 == -1:
            return
        data = self.a[self.t1]
        self.a[self.t1] = None
        self.t1 -= 1
        return data
    
    def peek(self):
        return self.a[self.t1]
    
    def len(self):
        count = 0
        while count < self.t1 + 1:
            count += 1
        return count
    
    def isEmpty(self):
        return self.t1 == -1
    
    def isFull(self):
        return self.t1 + 1 == self.limit
    
    def empty(self):
        for i in range(self.t1, -1, -1):
            self.a[i] = None
        self.t1 = -1


class P2():
    def __init__(self, a, n):
        self.t2 = n
        self.limit = n // 2
        self.a = a
    
    def push(self, data):
        if self.t2 == self.limit:
            return
        self.t2 -= 1
        self.a[self.t2] = data
    
    def pop(self):
        if self.t2 == len(self.a):
            return
        data = self.a[self.t2]
        self.a[self.t2] = None
        self.t2 += 1
        return data
    
    def peek(self):
        return self.a[self.t2]
    
    def len(self):
        count = 0
        while count < self.t2:
            count += 1
        return len(self.a) - count
    
    def isEmpty(self):
        return self.t2 == len(self.a)
    
    def isFull(self):
        return self.t2 == len(self.a) // 2
    
    def empty(self):
        length = len(self.a)
        for i in range(self.t2, length):
            self.a[i] = None
        self.t2 = length


# Q7 V2
class StackQ7():
    def __init__(self, n):
        self.t1 = -1
        self.t2 = n
        self.limit = n // 2
        self.a = [None] * n
        self.n = n
    
    def push(self, p, data):
        if p == 1:
            if self.t1 + 1 == self.limit:
                return
            self.t1 += 1
            self.a[self.t1] = data
        elif p == 2:
            if self.t2 == self.limit:
                return
            self.t2 -= 1
            self.a[self.t2] = data
    
    def pop(self, p):
        if p == 1:
            if self.t1 == -1:
                return
            data = self.a[self.t1]
            self.a[self.t1] = None
            self.t1 -= 1
            return data
        elif p == 2:
            if self.t2 == self.n:
                return
            data = self.a[self.t2]
            self.a[self.t2] = None
            self.t2 += 1
            return data
    
    def peek(self, p):
        if p == 1:
            if self.t1 == -1:
                return
            return self.a[self.t1]
        elif p == 2:
            if self.t2 == self.n:
                return
            return self.a[self.t2]
    
    def isEmpty(self, p):
        if p == 1:
            return self.t1 == -1
        elif p == 2:
            return self.t2 == self.n
    
    def isFull(self, p):
        if p == 1:
            return self.t1 == self.limit - 1
        elif p == 2:
            return self.t2 == self.limit
    
    def empty(self, p):
        if p == 1:
            for i in range(self.t1, -1, -1):
                self.a[i] = None
            self.t1 = -1
        elif p == 2:
            for i in range(self.t2, self.n):
                self.a[i] = None
            self.t2 = self.n
    
    def len(self, p):
        if p == 1:
            return self.t1 + 1
        elif p == 2:
            return self.n - self.t2
