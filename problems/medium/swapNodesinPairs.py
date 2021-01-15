'''
Given a linked list, swap every two adjacent nodes and return its head.

Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:
Input: head = []
Output: []

Example 3:
Input: head = [1]
Output: [1]
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def addToLinkedList(self, new_data):
        temp = Node(new_data)
        temp.next = self.head
        self.head = temp
    
    def printList(self):
        if self.head is None:
            print("The list is empty. Nothing to print")
        else:
            current = self.head
            while current is not None:
                print(current.value)
                current = current.next

    def swapNodesinPairs(self):
        length = 0
        if self.head is None:
            print("[]")
        else:
            current = self.head
            while current is not None:
                length += 1
                current = current.next
            
            
            first = self.head
            second = first.next
            



obj = SLL()
l = [1,2,3,4]

for i in l[::-1]:
    obj.addToLinkedList(i)
obj.printList()