from data_structures.stack import Stack


# Slide 12-13
def is_math_expression_valid(expression):
    stack = Stack()
    brackets = {')': '(', ']': '[', '}': '{'}
    for char in expression:
        if char in brackets.values():
            stack.push(char)
        elif char in brackets.keys():
            if stack.isEmpty() or stack.pop() != brackets[char]:
                return False
    return stack.is_empty()


# Slide 14
def is_html_valid(html):
    stack = Stack()
    begin = end = 0
    valid_tags = {'body', 'h1', 'center', 'p', 'ol', 'li'}
    if not html.startswith('<') or not html.endswith('>'):
        return False
    while True:
        begin = html.find('<', end)
        end = html.find('>', begin + 1)
        if begin == -1 or end == -1:
            break
        tag = html[begin: end + 1]
        if tag[1] != '/':
            if tag[1:-1] not in valid_tags:
                return False
            stack.push(tag)
        elif stack.is_empty() or stack.pop() != tag.replace('/', ''):
            return False
    return stack.is_empty()


# Slide 15-19
def infix_to_postfix(infix):
    postfix = ''
    priority = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    operators = Stack()
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
            while not operators.is_empty() and priority[operators.peek()] >= priority[char]:
                postfix += operators.pop()
            operators.push(char)
    while not operators.is_empty():
        postfix += operators.pop()
    return postfix


# Slide 20-21
def evaluate_postfix(postfix):
    operands = Stack()
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
def evaluate_infix(infix):
    postfix = ''
    stack = Stack()
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
def is_palindrome(string):
    stack = Stack()
    half = len(string) // 2
    for i in range(len(string)):
        if i < half:
            stack.push(string[i])
        elif len(string) % 2 and i == half:
            continue
        elif stack.pop() != string[i]:
            return False
    return stack.is_empty()


# Slide 25
def postfix_to_infix(postfix):
    operands = Stack()
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
