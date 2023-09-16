from Node import Node

class Stack():
    def __init__(self, data = None):
        self.top = None
        if data:
            for element in data:
                self.push(element)
    
    def __repr__(self):
        result = ''
        current = self.top
        while current:
            result += str(current.data) + '\n'
            current = current.next
        return result
    
    def __str__(self):
        return self.__repr__()
    
    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node
    
    def pop(self):
        if self.top == None:
            raise IndexError('The stack is empty.')
        node = self.top.data
        self.top = self.top.next
        return node
    
    def peek(self):
        if self.top == None:
            raise IndexError('The stack is empty.')
        return self.top.data
    
    def isMathExpressionValid(self, expression):
        brackets = {')': '(', ']': '[', '}': '{'}
        for char in expression:
            if char in brackets.values():
                self.push(char)
            elif char in brackets.keys():
                if self.top == None or self.pop() != brackets[char]:
                    return False
        return self.top == None
    
    def isHtmlValid(self, html):
        begin = end = 0
        while True:
            begin = html.find('<', end)
            end = html.find('>', begin + 1)
            tag = html[begin : end + 1]
            if begin == -1 or end == -1:
                break
            if tag[1] != '/':
                self.push(tag)
            elif self.top == None or self.pop() != tag.replace('/', ''):
                return False
        return self.top == None
    
    def isPalindrome(self, string):
        half = len(string) // 2
        for i in range(len(string)):
            if i < half:
                self.push(string[i])
            elif len(string) % 2 and i == half:
                continue
            elif self.pop() != string[i]:
                return False
        return self.top == None

