# This program creates a binary tree from provided inorder and preorder traversals.

''' Given:
    pre-order traversal =   [1, 2, 4, 8, 9, 10, 11, 5, 3, 6, 7] => goes Root, left, right
    in-order traversal =    [8, 4, 10, 9 11, 2, 5, 1, 6, 3, 7]  => goes left, Root, right

    ALGORITHM:
    1. Suppose the method is called buildTree with preorder and inorder lists.
    2. root := first node from the preorder, and delete first node from preorder
    3. root_index := index of root.val from the inorder list
    4. left or root := buildTree(preorder, subset of inorder from 0 to root_index)
    5. right or root := buildTree(preorder, subset of inorder from root_index + 1 to end)  
'''

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Method to print the tree using inorder traversal
def inOrderTraversal(root):
    if root is not None:
        inOrderTraversal(root.left)
        print(root.val, end=' ')
        inOrderTraversal(root.right)

class Solution:
    def buildTree(self, preorder, inorder):
        if inorder:
            root = TreeNode(preorder.pop(0))
            root_index = inorder.index(root.val)
            root.left = self.buildTree(preorder, inorder[:root_index])
            root.right = self.buildTree(preorder, inorder[root_index + 1:])
            return root

a = Solution()
inOrderTraversal(a.buildTree([1, 2, 4, 8, 9, 10, 11, 5, 3, 6, 7], [8, 4, 10, 9, 11, 2, 5, 1, 6, 3, 7]))