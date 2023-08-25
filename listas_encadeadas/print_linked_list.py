from LinkedList import LinkedList
from Node import Node

def printLinkedList(linkedList):
    currentElement = linkedList.head
    if currentElement.data == None:
        return
    if linkedList.length == 1:
        print(f'{currentElement.data}, ', end = '')
        return
    while currentElement.next != None:
        print(f'{currentElement.data}, ', end = '')
        currentElement = currentElement.next
    print(currentElement.data)


list = LinkedList()
list.setHead(Node(24))
list.insertAtEnd('agosto')
list.insertAtEnd(2023)

printLinkedList(list)
