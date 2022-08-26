class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preorder(node):
    if node:
        print(node.data, end = '')
        preorder(node.left)
        preorder(node.right)

def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end = '')
        inorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end = '')



tree = Node('+')
tree.left = Node('*')
tree.right = Node('E')
tree.left.left = Node('*')
tree.left.right = Node('D')
tree.left.left.left = Node('/')
tree.left.left.right = Node('C')
tree.left.left.left.left = Node('A')
tree.left.left.left.right = Node('B')

preorder(tree)
print()
inorder(tree)
print()
postorder(tree)
