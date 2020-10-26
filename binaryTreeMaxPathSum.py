'''Given a non-empty binary tree, find the maximum path sum.

For this problem: 
a path is defined as any node sequence from some starting node to any node in the tree along the parent-child connections. 
The path must contain at least one node and does not need to go through the root.
'''
l = []

class Node:
    def __init__(self, val, left=None, right=None):
        self.val    = val
        self.left   = left
        self.right  = right

def inOrderTraversal(root):
    if root is not None:
        inOrderTraversal(root.left)
        l.append(root.val)
        inOrderTraversal(root.right)
    return sum(l)

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

## Code the do all the above functions
r = Node(50) 
r = insert(r, 30) 
r = insert(r, 20) 
r = insert(r, 40) 
r = insert(r, 70) 
r = insert(r, 60) 
r = insert(r, 80)  

print("Max sum is: ", inOrderTraversal(r))