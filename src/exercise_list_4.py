from data_structures.queue import Queue


# Q11-A (Com recursividade)
def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)


# Q11-A (Sem recursividade)
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


# Q11-B (Com recursividade)
def sum_nodes(root):
    if root is None:
        return 0
    return root.data + sum_nodes(root.left) + sum_nodes(root.right)


# Q11-B (Sem recursividade)
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


# Q11-C (Com recursividade)
def depth(root):
    if root is None:
        return -1
    return 1 + max(depth(root.left), depth(root.right))


# Q11-C (Sem recursividade)
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
    return is_strict(root.left) and is_strict(root.right)


# Q12-B
def is_full(root):
    if root is None:
        return None
    if not root.left and not root.right:
        return True
    if not root.left or not root.right:
        return False
    return depth(root.left) == depth(root.right) and is_full(root.left) and is_full(root.right)


# Q12-C
def is_complete(root):
    if root is None:
        return None
    left_depth = depth(root.left)
    right_depth = depth(root.right)
    return abs(left_depth - right_depth) == 1
