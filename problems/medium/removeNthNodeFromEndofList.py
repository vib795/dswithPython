'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        

class SLL:
    def __init__(self):
        self.head = None
    
    def addToList(self, new_data):
        temp = Node(new_data)
        temp.next = self.head
        self.head = temp
        
    def printList(self):
        if self.head is None:
            print("[]")
        else:
            count = 1
            current = self.head
            while current is not None:
                print(current.data)
                count += 1
                current = current.next
    
    def getSize(self):
        current = self.head
        size = 0
        if self.head is None:
            return "The size of the list is 0."
        else:
            while current is not None:
                current = current.next
                size += 1
        return size

    def removeNthNodeFromEndOfList(self, n):
        if self.head is None:
            return "The list is empty."
        else:
            current = self.head
            length = 0
            while current is not None:
                current = current.next
                length +=1
            # print(length)

            # element to delete from the list 
            eleCount = 1
            # print(eleCount)
            current = self.head
            if length == 1:
                self.head = None
                # return("only one was available to remove.")
            else:
                while eleCount != (length - n):
                    current = current.next
                    eleCount += 1
                # print("Current data: ", current.data)
                current.next = current.next.next

            

obj = SLL()
l = [1,2,3,4,5,]
for i in l[::-1]:
    obj.addToList(i)
# obj.printList()
# print("\n")
# print(obj.getSize())
obj.removeNthNodeFromEndOfList(2)
obj.printList()
# print(obj.getSize())