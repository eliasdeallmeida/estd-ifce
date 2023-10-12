from data_structures.stack import Stack
from data_structures.queue import Queue


# Questões que podem estar na prova 03 (Pilhas e Filas)

# 1) Dado uma pilha P e um valor K, identifique se K está contido na pilha usando uma fila F.
def is_contained(stack, k):
    queue = Queue()
    while not stack.is_empty():
        queue.enqueue(stack.pop())
        if queue.rear.data == k:
            return True
    return False


stack = Stack(1, 2, 3, 4, 5)
print(is_contained(stack, 55))


# 2) Retorne todos os anagramas de uma palavra usando uma pilha.
def anagrams(word):
    stack = Stack()
    stack.push('+' + word)
    permutations = []
    while not stack.is_empty():
        current_str = stack.pop()
        marker_index = current_str.find('+')
        remaining_chars = current_str[marker_index + 1:]
        for char in remaining_chars:
            new_str = current_str[:marker_index] + char + \
                '+' + remaining_chars.replace(char, '', 1)
            stack.push(new_str)
        if current_str.replace('+', '') not in permutations:
            permutations.append(current_str.replace('+', ''))
    return permutations


print(anagrams('ABC'))


# 3) Retorne todos os subconjuntos de uma palavra usando uma pilha e uma fila.
def subsets(word):
    stack = Stack()
    permutations = Queue()
    stack.push('+' + word)
    while not stack.is_empty():
        current_str = stack.pop()
        marker_index = current_str.find('+')
        remaining_chars = current_str[marker_index + 1:]
        for char in remaining_chars:
            new_str = current_str[:marker_index] + char + \
                '+' + remaining_chars.replace(char, '', 1)
            stack.push(new_str)
        is_contained = False
        current_node = permutations.front
        while current_node and not is_contained:
            if current_str[:marker_index] == current_node.data:
                is_contained = True
            current_node = current_node.next
        if not is_contained:
            permutations.enqueue(current_str[:marker_index])
    return permutations


print(subsets('ABC'))
