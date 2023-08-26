from LinkedList import LinkedList

list = LinkedList()
list.insertAtBeginning('IFCE')
list.insertAtEnd(25)
list.insertAtEnd('agosto')
list.insertAtEnd(2023)
list.insertAtEnd('estrutura')
list.insertAtEnd('de')
list.insertAtEnd('dados')
list.insertAtEnd(2023)

print(f'Tamanho da lista encadeada: {list.length}')
list.printElements()
print()

list.removeAtBeginning()
list.printElements()
print()

list.removeAtGivenPosition(2)
list.printElements()
print()

list.removeElementsByValue(2023)
list.printElements()
