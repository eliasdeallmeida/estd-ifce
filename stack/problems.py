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
    pass


# Slide 20-21
def calculatePostfix(postfix):
    stack = StackWithLinkedList()
    for char in postfix:
        if char == '+':
            stack.push(stack.pop() + stack.pop())
        elif char == '-':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.push(n2 - n1)
        elif char == '*':
            stack.push(stack.pop() * stack.pop())
        elif char == '/':
            stack.push(stack.pop() / stack.pop())
        else:
            stack.push(int(char))
    return stack.peek()


# Slide 22
def calculateInfix(infix):
    pass


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
    pass
