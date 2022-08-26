class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def print_tree(node):
    if node:
        print(node.data, end = ' ')
        print_tree(node.left)
        print_tree(node.right)


n = int(input())
arr = list(map(int, input().split()))
tree = [Node(i) for i in range(n+1)]
# tree[1] = Node(1), tree[2] = Node(2) ....
for i in range(0, (n-1)*2, 2):
    if tree[arr[i]].left == None:
        tree[arr[i]].left = tree[arr[i+1]]
    else:
        tree[arr[i]].right = tree[arr[i + 1]]

print_tree(tree[1])