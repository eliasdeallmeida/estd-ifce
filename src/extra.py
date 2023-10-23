from data_structures.stack import Stack
from data_structures.queue import Queue
from data_structures.binary_tree import BinaryTree
from exercise_list_4 import depth, count_nodes


# Questões que podem estar na prova 02 (Pilhas e Filas)

# 1) Identifique se um valor k está contido em uma pilha usando uma fila.
def is_contained(stack, k):
    queue = Queue()
    while not stack.is_empty():
        queue.enqueue(stack.pop())
        if queue.rear.data == k:
            return True
    return False


stack = Stack(1, 2, 3, 4, 5)
# print(is_contained(stack, 55))


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


# print(anagrams('ABC'))


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


# print(subsets('ABC'))


bt = BinaryTree('A')
bt.root.set_left('B')
bt.root.set_right('C')
bt.root.left.set_left('D')
bt.root.left.set_right('E')
bt.root.right.set_left('F')
# bt.root.set_left(12)
# bt.root.set_right(8)
# bt.root.left.set_left(5)
# bt.root.left.set_right(2)
# bt.root.right.set_right(123)


# Verificar se uma árvore binária é balanceada
def is_balanced(root):
    if root is None:
        return True
    left_height = depth(root.left)
    right_height = depth(root.right)
    is_left_balanced = is_balanced(root.left)
    is_right_balanced = is_balanced(root.right)
    if abs(left_height - right_height) <= 1 and is_left_balanced and is_right_balanced:
        return True
    return False


# print(is_balanced(bt.root))


# Verificar se uma árvore binária é perfeitamente balanceada
def is_perfectly_balanced(root):
    if root is None:
        return True
    nodes_left = count_nodes(root.left)
    nodes_right = count_nodes(root.right)
    is_left_perfectly_balanced = is_perfectly_balanced(root.left)
    is_right_perfecly_balanced = is_perfectly_balanced(root.right)
    if abs(nodes_left - nodes_right) <= 1 and is_left_perfectly_balanced and is_right_perfecly_balanced:
        return True
    return False


# print(is_perfectly_balanced(bt.root))


def display_by_level(root):
    if root is None:
        return None
    queue = Queue(root)
    while not queue.is_empty():
        node = queue.dequeue()
        print(node.data, end=' ')
        if node.left:
            queue.enqueue(node.left)
        if node.right:
            queue.enqueue(node.right)


# display_by_level(bt.root)


def count_n(root, n):
    if root is None:
        return 0
    if root.data != n:
        return count_n(root.left, n) + count_n(root.right, n)
    return 1 + count_n(root.left, n) + count_n(root.right, n)


# print(count_n(bt.root, 5))
