from data_structures.stack import Stack


# Q1
# 3, 8, 2, 1, 6, 7, 4, 1


# Q2
# tam = 25 - (10 - 3)
# tam = 25 - 7
# tam = 18
# Logo, no final das operações, a pilha terá 18 elementos


# Q3
def transfer(s, t):
    while not s.is_empty():
        t.push(s.pop())


# Q4
def empty(stack):
    if stack.is_empty():
        return
    stack.pop()
    empty(stack)


# Q5 V1 (Com retorno)
def reverse_array(array):
    stack = Stack()
    reverse = []
    for element in array:
        stack.push(element)
    for _ in range(len(array)):
        reverse.append(stack.pop())
    return reverse


# Q5 V2 (Sem retorno)
def reverse_array(array):
    stack = Stack()
    for element in array:
        stack.push(element)
    for i in range(len(array)):
        array.insert(i, stack.pop())
        array.pop()


# Q6
class StackQ6():
    def __init__(self, n):
        self.n = n
        self.a = [None] * n
        self.a[0] = 0

    def push(self, data):
        if self.is_full():
            return
        self.a[0] += 1
        self.a[self.a[0]] = data

    def pop(self):
        if self.is_empty():
            return
        data = self.a[self.a[0]]
        self.a[self.a[0]] = None
        self.a[0] -= 1
        return data

    def peek(self):
        return self.a[self.a[0]]

    def is_empty(self):
        return self.a[0] == 0

    def is_full(self):
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
        if self.is_full() or data > 0:
            return
        if p == 1:
            self.t1 += 1
            self.a[self.t1] = data
        elif p == 2:
            self.t2 -= 1
            self.a[self.t2] = data

    def pop(self, p):
        if self.is_empty(p):
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
        if self.is_empty(p):
            return
        if p == 1:
            return self.a[self.t1]
        elif p == 2:
            return self.a[self.t2]

    def is_empty(self, p):
        if p == 1:
            return self.t1 == -1
        elif p == 2:
            return self.t2 == self.n

    def is_full(self):
        return self.t1 + 1 == self.t2

    def empty(self, p):
        if p == 1:
            self.a[:self.t1 + 1] = [None] * (self.t1 + 1)
            self.t1 = -1
        elif p == 2:
            self.a[self.t2:] = [None] * (self.n - self.t2)
            self.t2 = self.n

    def len(self, p):
        if p == 1:
            return self.t1 + 1
        elif p == 2:
            return self.n - self.t2


# Q8
def evaluate_expression(expression):
    stack = Stack()
    count = 0
    for char in expression:
        if char.isalpha():
            stack.push(char)
        else:
            if char == '+':
                operation = 'AD '
            elif char == '-':
                operation = 'SB '
            elif char == '*':
                operation = 'ML '
            elif char == '/':
                operation = 'DV '
            count += 1
            n2 = stack.pop()
            n1 = stack.pop()
            stack.push('TEMP' + str(count))
            print('LD ' + n1)
            print(operation + n2)
            print('ST TEMP' + str(count))
