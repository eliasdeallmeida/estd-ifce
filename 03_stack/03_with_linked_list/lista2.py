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
        if self.isFull():
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
    
    def len(self):
        return self.a[0]


# Q7
class StackQ7():
    def __init__(self, n):
        self.t1 = -1
        self.t2 = n
        self.a = [None] * n
        self.n = n
    
    def __str__(self):
        return str(self.a)
    
    def push(self, p, data):
        if self.isFull() or data > 0:
            return
        if p == 1:
            self.t1 += 1
            self.a[self.t1] = data
        elif p == 2:
            self.t2 -= 1
            self.a[self.t2] = data
    
    def pop(self, p):
        if self.isEmpty(p):
            return
        if p == 1:
            data = self.a[self.t1]
            self.a[self.t1] = None
            self.t1 -= 1
            return data
        elif p == 2:
            data = self.a[self.t2]
            self.a[self.t2] = None
            self.t2 += 1
            return data
    
    def peek(self, p):
        if self.isEmpty(p):
            return
        if p == 1:
            return self.a[self.t1]
        elif p == 2:
            return self.a[self.t2]
    
    def isEmpty(self, p):
        if p == 1:
            return self.t1 == -1
        elif p == 2:
            return self.t2 == self.n
    
    def isFull(self):
        return self.t1 + 1 == self.t2
    
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


# Q8
def avaliarExpressao(expressao):
    pilha = Stack()
    count = 0
    for char in expressao:
        if char.isalpha():
            pilha.push(char)
        else:
            if char == '+':
                op = 'AD '
            elif char == '-':
                op = 'SB '
            elif char == '*':
                op = 'ML '
            elif char == '/':
                op = 'DV '
            count += 1
            op2 = pilha.pop()
            op1 = pilha.pop()
            pilha.push('TEMP' + str(count))
            print('LD ' + op1)
            print(op + op2)
            print('ST TEMP' + str(count))
