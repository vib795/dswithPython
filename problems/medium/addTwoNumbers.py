'''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
'''
class SllNode:
    def __init__(self, data):
        self.data   = data
        self.next   = None

class SLL:
    def __init__(self):
        self.head   = None

    def append(self, data):
        if self.head == None:
            print("Adding the first element in the list...")
            temp = SllNode(data)
            self.head = temp
            temp.next = None
        else:
            current = self.head
            temp = SllNode(data)
            previous = self.head
            while current is not None:
                previous = current
                # print("Previous", previous)
                current = current.next
                # print("Current", current)
            previous.next = temp

    def printList(self):
        if self.head is None:
            print("The list is empty. Nothing to print.")
        else:
            current = self.head
            while current is not None:
                print(current.data)
                current = current.next
        pass

class AddLL(SLL):
    pass

l1 = [2,4,3]
l2 = [5,6,4]

l1.reverse()
l2.reverse()

SLLObj1 = SLL()
SLLObj2 = SLL()

for i in l1:
    SLLObj1.append(i)
SLLObj1.printList()
for i in l2:
    SLLObj2.append(i)
SLLObj2.printList()
