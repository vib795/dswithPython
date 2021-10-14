'''
Given an array of strings products and a string searchWord. We want to design a system that suggests at most three product names from products after each character of searchWord is typed. 
Suggested products should have common prefix with the searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return list of lists of the suggested products after each character of searchWord is typed. 
Example 1:
Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]

Example 2:
Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]

Example 3:
Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]

Example 4:
Input: products = ["havana"], searchWord = "tatiana"
Output: [[],[],[],[],[],[],[]]
'''
class Node:
    def __init__(self, key):
        self.val    =   key
        self.left   =   None
        self.right  =   None

def insert(root, key):
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

# # In - order traversal on the BST - LEFT -> ROOT -> RIGHT
# def inOrderTraversal(root):
#     if root:
#         inOrderTraversal(root.left)
#         print(root.val)
#         inOrderTraversal(root.right)

products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = list("mouse")
print(searchWord)
r = Node(searchWord[0])
for i in range(1, len(searchWord)):
    r = insert(r, searchWord[i])

# # Print in - oder traversal of the BST 
# print("Here is the in - order traversal:")
# inOrderTraversal(r)