from random import randint
from data_structures.binary_tree import Node
from data_structures.queue import Queue


# Slide 32
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


# Slide 33
def biggest_value(root):
    biggest_value = root.data
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
def biggest_value(root):
    if root is None:
        return None
    if not root.left and not root.right:
        return root.data
    return max(root.data, biggest_value(root.left), biggest_value(root.right))


# Slide 35
def has_value(root, value):
    if root is None:
        return False
    if root.data == value:
        return True
    return has_value(root.left, value) or has_value(root.right, value)


# Slide 36
def has_value(root, value):
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
