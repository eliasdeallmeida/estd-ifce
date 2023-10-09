from StackWithLinkedList import StackWithLinkedList


# Slide 12-13
def isMathExpressionValid(expression):
    stack = StackWithLinkedList()
    brackets = {')': '(', ']': '[', '}': '{'}
    for char in expression:
        if char in brackets.values():
            stack.push(char)
        elif char in brackets.keys():
            if stack.isEmpty() or stack.pop() != brackets[char]:
                return False
    return stack.isEmpty()


# Slide 14
def isHtmlValid(html):
    stack = StackWithLinkedList()
    begin = end = 0
    validTags = {'body', 'h1', 'center', 'p', 'ol', 'li'}
    if not html.startswith('<') or not html.endswith('>'):
        return False
    while True:
        begin = html.find('<', end)
        end = html.find('>', begin + 1)        
        if begin == -1 or end == -1:
            break
        tag = html[begin : end + 1]
        if tag[1] != '/':
            if tag[1:-1] not in validTags:
                return False
            stack.push(tag)
        elif stack.isEmpty() or stack.pop() != tag.replace('/',''):
            return False
    return stack.isEmpty()


# Slide 15-19
def infixToPostfix(infix):
    postfix = ''
    priority = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    operators = StackWithLinkedList()
    for char in infix:
        if char.isalpha():
            postfix += char
        elif char == '(':
            operators.push(char)
        elif char == ')':
            while operators.peek() != '(':
                postfix += operators.pop()
            operators.pop()
        elif char in '+-*/^':
            while not operators.isEmpty() and priority[operators.peek()] >= priority[char]:
                postfix += operators.pop()
            operators.push(char)
    while not operators.isEmpty():
        postfix += operators.pop()
    return postfix


# Slide 20-21
def evaluatePostfix(postfix):
    operands = StackWithLinkedList()
    for char in postfix:
        if char in '+-*/':
            n2 = operands.pop()
            n1 = operands.pop()
            if char == '+':
                operands.push(n1 + n2)
            elif char == '-':
                operands.push(n1 - n2)
            elif char == '*':
                operands.push(n1 * n2)
            elif char == '/':
                operands.push(n1 / n2)
        else:
            operands.push(int(char))
    return operands.pop()


# Slide 22
def evaluateInfix(infix):
    postfix = ''
    stack = StackWithLinkedList()
    for char in infix:
        postfix = char + postfix
    for char in postfix:
        if char == '+':
            stack.push(stack.pop() + stack.pop())
        elif char == '-':
            stack.push(stack.pop() - stack.pop())
        elif char == '*':
            stack.push(stack.pop() * stack.pop())
        elif char == '/':
            stack.push(stack.pop() / stack.pop())
        else:
            stack.push(int(char))
    return stack.pop()


# Slide 23-24
def isPalindrome(string):
    stack = StackWithLinkedList()
    half = len(string) // 2
    for i in range(len(string)):
        if i < half:
            stack.push(string[i])
        elif len(string) % 2 and i == half:
            continue
        elif stack.pop() != string[i]:
            return False
    return stack.isEmpty()


# Slide 25
def postfixToInfix(postfix):
    infix = ''
    operands = StackWithLinkedList()
    for char in postfix:
        if char.isalpha():
            operands.push(char)
        elif char in '+-*/':
            n2 = operands.pop()
            n1 = operands.pop()
            if char == '+':
                operands.push('(' + n1 + ' + ' + n2 + ')')
            elif char == '-':
                operands.push('(' + n1 + ' - ' + n2 + ')')
            elif char == '*':
                operands.push('(' + n1 + ' * ' + n2 + ')')
            elif char == '/':
                operands.push('(' + n1 + ' / ' + n2 + ')')
    return operands.pop()
