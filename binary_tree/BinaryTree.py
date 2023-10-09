class Node():
    def __init__(self, data, father = None, left = None, right = None, isLeft = False):
        self.data = data
        self.father = father
        self.left = left
        self.right = right
        self.isLeft = isLeft
    
    def setLeft(self, data):
        self.left = Node(data, self, isLeft = True)
    
    def setRight(self, data):
        self.right = Node(data, self)


class BinaryTree():
    def __init__(self, data = None):
        if data:
            self.root = Node(data)
        else:
            self.root = None
    
    def preOrder(self, root):
        if root == None:
            return
        print(root.data, sep = '->', end = '->')
        self.preOrder(root.left)
        self.preOrder(root.right)
    
    def inOrder(self, root):
        if root == None:
            return
        self.inOrder(root.left)
        print(root.data, sep = '->', end = '->')
        self.inOrder(root.right)
    
    def postOrder(self, root):
        if root == None:
            return
        self.postOrder(root.left)
        self.postOrder(root.right)
        print(root.data, sep = '->', end = '->')
