from DoublyLinkedList import DoublyLinkedList

list = DoublyLinkedList()
list.insertAtEnd(2023)
list.insertAtEnd(25)
list.insertAtEnd(8)
list.insertAtEnd('dados')

list.printElements()
print(f'Tamanho da lista: {list.length}')
print()

list.insertAtGivenPosition(2, 'estrutura')
list.printElements()
print(f'Tamanho da lista: {list.length}')
print()

list.removeAtGivenPosition(-2)
list.printElements()
print(f'Tamanho da lista: {list.length}')
print()