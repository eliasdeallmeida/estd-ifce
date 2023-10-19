from random import randint
from math import log2, floor
from data_structures.binary_tree import BinaryTree, Node
from data_structures.queue import Queue


# Slide 32
# Função não recursiva que gera uma árvore com valores aleatórios (com exceção da raiz).
def build_random_tree(root_value, number_of_nodes):
    if number_of_nodes == 0:
        return None
    root = Node(root_value)
    queue = Queue(root)
    count = 1
    while count < number_of_nodes:
        node = queue.dequeue()
        node.set_left(randint(1, 10))
        count += 1
        if count == number_of_nodes:
            break
        node.set_right(randint(1, 10))
        count += 1
        if count == number_of_nodes:
            break
        queue.enqueue(node.left)
        queue.enqueue(node.right)
    return root


# Função recursiva que gera uma árvore com valores aleatórios (com exceção da raiz).
# (OBS: Foi necessário adicionar novos parâmetros, adicionar mais um retorno, usar funções adicionais
# para calcular a profundidade máxima da árvore e o máximo de nós que ficarão no último nível)
def max_nodes_in_last_level(number_of_nodes):
    sum = depth = max_of_nodes = 0
    while sum < number_of_nodes:
        max_of_nodes = 2**depth
        if sum + max_of_nodes > number_of_nodes:
            max_of_nodes = number_of_nodes - sum
            break
        sum += max_of_nodes
        depth += 1
    return max_of_nodes


def build(n, root_value, depth=0, nodes_last_level=0, max=None):
    if n == 0:
        return None
    if max is None:
        max = max_nodes_in_last_level(n)
    root = Node(root_value)
    if depth > floor(log2(n)):
        return None, 0
    if depth == floor(log2(n)):
        if nodes_last_level == max:
            return None, nodes_last_level
        return root, nodes_last_level + 1
    root.left, nodes_last_level = build(
        n, randint(1, 10), depth + 1, nodes_last_level)
    root.right, nodes_last_level = build(
        n, randint(1, 10), depth + 1, nodes_last_level)
    return root, nodes_last_level


# Slide 33
def biggest_value_with_queue(root):
    biggest_value = None
    queue = Queue(root)
    while not queue.is_empty():
        node = queue.dequeue()
        if not biggest_value or node.data > biggest_value:
            biggest_value = node.data
        if node.left:
            queue.enqueue(node.left)
        if node.right:
            queue.enqueue(node.right)
    return biggest_value


# Slide 34
def biggest_value_with_recursion(root, biggest=None):
    if root is None:
        return None
    if not root.left and not root.right:
        if biggest is None or root.data > biggest:
            return root.data
        return biggest
    if root.left and not root.right:
        left_biggest_value = biggest_value_with_recursion(root.left, biggest)
        return max(root.data, left_biggest_value)
    if not root.left and root.right:
        right_biggest_value = biggest_value_with_recursion(root.right, biggest)
        return max(root.data, right_biggest_value)
    if root.left and root.right:
        left_biggest_value = biggest_value_with_recursion(root.left, biggest)
        right_biggest_value = biggest_value_with_recursion(root.right, biggest)
        return max(root.data, left_biggest_value, right_biggest_value)


# Slide 35
def has_value_with_recursion(root, value):
    if root is None:
        return None
    if root.data == value:
        return True
    if root.left and not root.right:
        return has_value_with_recursion(root.left, value)
    if not root.left and root.right:
        return has_value_with_recursion(root.right, value)
    if root.left and root.right:
        has_value_on_left = has_value_with_recursion(root.left, value)
        has_value_on_right = has_value_with_recursion(root.right, value)
        return has_value_on_left or has_value_on_right
    return False


# Slide 36
def has_value_wtih_queue(root, value):
    if root is None:
        return None
    queue = Queue(root)
    while not queue.is_empty():
        node = queue.dequeue()
        if node.data == value:
            return True
        if node.left:
            queue.enqueue(node.left)
        if node.right:
            queue.enqueue(node.right)
    return False
