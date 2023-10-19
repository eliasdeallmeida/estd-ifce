from data_structures.binary_tree import BinaryTree
from data_structures.queue import Queue


# Q11-A (com recursividade)
def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)


# Q11-A (sem recursividade)
def count_nodes(root):
    if root is None:
        return 0
    count = 0
    queue = Queue(root)
    while not queue.is_empty():
        node = queue.dequeue()
        count += 1
        if node.left:
            queue.enqueue(node.left)
        if node.right:
            queue.enqueue(node.right)
    return count


# Q11-B (com recursividade)
def sum_nodes(root):
    if not root.left and not root.right:
        return root.data
    if root.left and not root.right:
        return root.data + sum_nodes(root.left)
    if not root.left and root.right:
        return root.data + sum_nodes(root.right)
    if root.left and root.right:
        return root.data + sum_nodes(root.left) + sum_nodes(root.right)
    return None


# Q11-B (sem recursividade)
def sum_nodes(root):
    if root is None:
        return 0
    sum = 0
    queue = Queue(root)
    while not queue.is_empty():
        node = queue.dequeue()
        sum += node.data
        if node.left:
            queue.enqueue(node.left)
        if node.right:
            queue.enqueue(node.right)
    return sum


# Q11-C (com recursividade)
def depth(root):
    if root is None:
        return -1
    left_depth = depth(root.left)
    right_depth = depth(root.right)
    return 1 + max(left_depth, right_depth)


# Q11-C (sem recursividade)
def depth(root):
    depth = -1
    if root is None:
        return depth
    queue = Queue(root)
    while not queue.is_empty():
        depth += 1
        for _ in range(queue.size):
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
    return depth


# Q12-A
def is_strict(root):
    if root is None:
        return None
    if not root.left and not root.right:
        return True
    if not root.left or not root.right:
        return False
    if root.left and root.right:
        return is_strict(root.left) and is_strict(root.right)


# Q12-B
# Implementação da função is_full() com o uso da função depth(), mas sem o uso de parâmetros adicionais
def is_full(root):
    if root is None:
        return None
    if not root.left and not root.right:
        return True
    if not root.left or not root.right:
        return False
    if root.left and root.right:
        left_depth = depth(root.left)
        right_depth = depth(root.right)
        is_left_full = is_full(root.left)
        is_right_full = is_full(root.right)
        return left_depth == right_depth and is_left_full and is_right_full


# Implementação da função is_full() sem o uso da função depth(), mas com o uso de parâmatros adicionais
# def is_full(root, left_depth=0, right_depth=0):
#     if root is None:
#         return None
#     if not root.left and not root.right:
#         return True
#     if not root.left and root.right or root.left and not root.right:
#         return False
#     if root.left and root.right:
#         is_left_strict = is_full(root.left, left_depth + 1, right_depth)
#         is_right_stric = is_full(root.right, left_depth, right_depth + 1)
#         return left_depth == right_depth and is_left_strict and is_right_strict


# Q12-C
# Implementação da função is_complete() com o uso da função depth()
def is_complete(root):
    if root is None:
        return None
    left_depth = depth(root.left)
    right_depth = depth(root.right)
    return abs(left_depth - right_depth) == 1


# Implementação da função is_complete() sem o uso da função depth()
# (OBS: Apresenta problemas com determinadas quantidades de nós)
# def is_complete(root):
#     if root is None:
#         return None
#     if not root.left and not root.right:
#         return 1
#     if root.left and not root.right:
#         return 1 + is_complete(root.left)
#     if not root.left and root.right:
#         return 1 + is_complete(root.right)
#     if root.left and root.right:
#         left_depth = 1 + is_complete(root.left)
#         right_depth = 1 + is_complete(root.right)
#         return abs(left_depth - right_depth) == 1
