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
            # print("Adding the first element in the list...")
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
        l = []
        if self.head is None:
            print("The list is empty. Nothing to print.")
        else:
            current = self.head
            while current is not None:
                l.append(current.data)
                # print(current.data)
                current = current.next
            return l

    def addTwoLists(self, first, second):
        prev = None
        temp = None
        carry = 0
 
        # While both list exists
        while(first is not None or second is not None):
            fdata = 0 if first is None else first.data
            sdata = 0 if second is None else second.data
            Sum = carry + fdata + sdata
 
            # update carry for next calculation
            carry = 1 if Sum >= 10 else 0
 
            # update sum if it is greater than 10
            Sum = Sum if Sum < 10 else Sum % 10
 
            # Create a new node with sum as data
            temp = SllNode(Sum)
 
            # if this is the first node then set it as head
            # of resultant list
            if self.head is None:
                self.head = temp
            else:
                prev.next = temp
 
            # Set prev for next insertion
            prev = temp
 
            # Move first and second pointers to next nodes
            if first is not None:
                first = first.next
            if second is not None:
                second = second.next
 
        if carry > 0:
            temp.next = SllNode(carry)

# l1 = [2,4,3]
# l2 = [5,6,4]
# l1 = [0]
# l2 = [0]
l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]

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

# Add the two lists and see result
res = SLL()
res.addTwoLists(SLLObj1.head, SLLObj2.head)
# print("\nResultant list is\n")
print(res.printList())