from LinkedList import *
from DoublyLinkedList import *


# Slide 28-29
def getNthElement(linkedList, n):
    if n < 0 or n >= len(linkedList):
        raise IndexError('Invalid index given.')
    element = linkedList.head
    for _ in range(n):
        element = element.next
    return element.data


# Slide 32-33
def removeElementsByValue(linkedList, value):
    current = linkedList.head
    previous = None
    while current:
        if current.data == value:
            if previous == None:
                linkedList.head = current.next
            else:
                previous.next = current.next
            linkedList.size -= 1
        else:
            previous = current
        current = current.next


# Slide 34-37
def hasCycle(circularLinkedList):
    pass


# Slide 38
def findMiddle(linkedList):
    pointer = linkedList.head
    if len(linkedList) % 2:
        for _ in range(len(linkedList) // 2):
            pointer = pointer.next
        return pointer.data
    else:
        for _ in range(len(linkedList) // 2 - 1):
            pointer = pointer.next
        return [pointer.data, pointer.next.data]


# Slide 39
def reverseLinkedList(linkedList):
    if len(linkedList) <= 1:
        return
    current = linkedList.head
    previous = None
    while current.next:
        next = current.next
        current.next = previous
        previous = current
        current = next
    current.next = previous
    linkedList.head = current


# Slide 40
def reverseInPairs(linkedList):
    current = linkedList.head
    while current and current.next:
        currentCopy = current.data
        current.data = current.next.data
        current.next.data = currentCopy
        current = current.next.next


# Slide 41
def removeRepetitions(linkedList):
    current = linkedList.head
    while current.next:
        if current.data == current.next.data:
            current.next = current.next.next
            linkedList.size -= 1
        else:
            current = current.next


# Slide 42
def reverseAtGivenElement(current):
    reverseList = LinkedList()
    while current:
        reverseList.insertAtBeginning(current.data)
        current = current.next
    return reverseList.head


def isPalindrome(linkedList):
    if len(linkedList) == 0:
        return False
    if len(linkedList) == 1:
        return True
    current = firstHalf = linkedList.head
    for _ in range(linkedList.size // 2):
        current = current.next
    if linkedList.size % 2:
        secondHalf = reverseAtGivenElement(current.next)
    else:
        secondHalf = reverseAtGivenElement(current)
    while secondHalf:
        if firstHalf.data != secondHalf.data:
            return False
        firstHalf = firstHalf.next
        secondHalf = secondHalf.next
    return True
