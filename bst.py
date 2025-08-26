# Import libraries
from collections import deque
from graphviz import Digraph

# Node class
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Inorder traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

# Preorder traversal
def preorder(root):
    if root:
        print(root.key, end=" ")
        preorder(root.left)
        preorder(root.right)

# Postorder traversal
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.key, end=" ")

# Level-order traversal
def level_order(root):
    if not root:
        return
    q = deque([root])
    while q:
        node = q.popleft()
        print(node.key, end=" ")
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

# Insert key
def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    return root

# Search key
def search(root, key):
    if root is None or root.key == key:
        return root
    if key < root.key:
        return search(root.left, key)
    return search(root.right, key)

# Get successor node
def get_successor(node):
    curr = node.right
    while curr and curr.left:
        curr = curr.left
    return curr

# Delete key
def delete(root, key):
    if root is None:
        return root
    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        succ = get_successor(root)
        root.key = succ.key
        root.right = delete(root.right, succ.key)
    return root

# Minimum value
def minValue(root):
    curr = root
    while curr and curr.left:
        curr = curr.left
    return curr.key if curr else None

# Maximum value
def maxValue(root):
    curr = root
    while curr and curr.right:
        curr = curr.right
    return curr.key if curr else None

# Floor value
def floor(root, x):
    floor_val = None
    while root:
        if root.key == x:
            return root.key
        if root.key > x:
            root = root.left
        else:
            floor_val = root.key
            root = root.right
    return floor_val

# Ceil value
def ceil(root, x):
    ceil_val = None
    while root:
        if root.key == x:
            return root.key
        if root.key < x:
            root = root.right
        else:
            ceil_val = root.key
            root = root.left
    return ceil_val

# Leftmost node
def leftMost(node):
    while node.left:
        node = node.left
    return node

# Rightmost node
def rightMost(node):
    while node.right:
        node = node.right
    return node

# Successor
def getSuccessor(root, target):
    succ = None
    curr = root
    while curr:
        if target < curr.key:
            succ = curr
            curr = curr.left
        elif target > curr.key:
            curr = curr.right
        else:
            if curr.right:
                return leftMost(curr.right)
            break
    return succ

# Predecessor
def getPredecessor(root, target):
    pred = None
    curr = root
    while curr:
        if target > curr.key:
            pred = curr
            curr = curr.right
        elif target < curr.key:
            curr = curr.left
        else:
            if curr.left:
                return rightMost(curr.left)
            break
    return pred

# Height
def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))

# Count nodes
def count_nodes(root):
    if not root:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

# Count leaves
def count_leaves(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    return count_leaves(root.left) + count_leaves(root.right)

# Validate BST
def is_bst(root, low=float('-inf'), high=float('inf')):
    if not root:
        return True
    if not (low < root.key < high):
        return False
    return is_bst(root.left, low, root.key) and is_bst(root.right, root.key, high)

# Path to node
def path_to_node(root, key):
    path = []
    curr = root
    while curr:
        path.append(curr.key)
        if key < curr.key:
            curr = curr.left
        elif key > curr.key:
            curr = curr.right
        else:
            return path
    return None

# Print tree
def print_tree(root, level=0, prefix="Root: "):
    if root:
        print(" " * (level*4) + prefix + str(root.key))
        if root.left or root.right:
            if root.left:
                print_tree(root.left, level+1, "L--- ")
            else:
                print(" " * ((level+1)*4) + "L--- None")
            if root.right:
                print_tree(root.right, level+1, "R--- ")
            else:
                print(" " * ((level+1)*4) + "R--- None")

# Visualize BST
def visualize_bst(root, filename="bst"):
    if not root:
        return None
    dot = Digraph()
    def add_nodes_edges(node):
        if not node:
            return
        dot.node(str(node.key), str(node.key))
        if node.left:
            dot.edge(str(node.key), str(node.left.key))
            add_nodes_edges(node.left)
        if node.right:
            dot.edge(str(node.key), str(node.right.key))
            add_nodes_edges(node.right)
    add_nodes_edges(root)
    dot.render(filename, format='png', cleanup=True)
    return f"{filename}.png"
