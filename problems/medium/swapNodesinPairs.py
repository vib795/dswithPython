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
            return("The list is empty. Nothing to print")
        else:
            l = []
            current = self.head
            while current is not None:
                # print(current.value)
                l.append(current.value)
                current = current.next
            return l

    def swapNodesinPairs(self):
        temp = self.head
        if self.head is None:
            print("Nothing to swap. The list is empty.")
        else:
            while temp is not None and temp.next is not None:
                if temp.value == temp.next.value:
                    temp = temp.next.next
                
                else:
                    temp.value, temp.next.value = temp.next.value, temp.value
                    temp = temp.next.next
            pass
        pass
            


# Driver code
obj = SLL()
l = [1,2,3,4,5]

for i in l[::-1]:
    obj.addToLinkedList(i)
print("Before:  ", obj.printList())
# obj.printList()
obj.swapNodesinPairs()
print("After:   ", obj.printList())