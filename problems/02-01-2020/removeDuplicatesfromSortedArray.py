'''
Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Clarification:
Confused why the returned value is an integer but your answer is an array?
Note that the input array is passed in by reference, which means a modification to the input array will be known to the caller as well.
'''

class removeDuplicatefromSortedArray:

    def __init__(self, nums):
        self.nums = nums

    def checkArraySorted(self):
        # Calculating length
        n = len(arr)
        # Array has one or no element or the
        # rest are already checked and approved.
        if n == 1 or n == 0:
            return True
 
        # Recursion applied till last element
        return arr[0] <= arr[1] and arraySortedOrNot(arr[1:])

    
    def sortArrayInPlace(self):
        pass