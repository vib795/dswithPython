# This program implements a BST (Binary Search Tree). Search and Insert values in the tree. 
class Node:
    def __init__(self, key):
        self.val = key
        self.right = None
        self.left = None

# Method to insert items in the BST
def insert(root,key): 
    if root is None: 
        return Node(key) 
    else:
        if root.val == key:
            return root
        elif root.val < key: 
            root.right = insert(root.right, key) 
        else:
            root.left = insert(root.left, key)
    return root

# In - order traversal on the BST - LEFT -> ROOT -> RIGHT
def inOrderTraversal(root):
    if root:
        inOrderTraversal(root.left)
        print(root.val)
        inOrderTraversal(root.right)

# Post - order traversal on the BST - LEFT -> RIGHT -> ROOT
def postOrderTraversal(root):
    if root:
        postOrderTraversal(root.left)
        postOrderTraversal(root.right)
        print(root.val)

# Pre - order traversal on the BST - ROOT -> LEFT -> RIGHT
def preOrderTraversal(root):
    if root:
        print(root.val)
        preOrderTraversal(root.left)
        preOrderTraversal(root.right)

## Code the do all the above functions
r = Node(50) 
r = insert(r, 30) 
r = insert(r, 20) 
r = insert(r, 40) 
r = insert(r, 70) 
r = insert(r, 60) 
r = insert(r, 80) 

# Print in - oder traversal of the BST 
print("Here is the in - order traversal:")
inOrderTraversal(r)

# Print post - order traversal of the BST
print("\nHere is the post - order traversal:")
postOrderTraversal(r)

# Print pre - order traversal of the BST
print("\nHere is the pre - order traversal:")
preOrderTraversal(r)