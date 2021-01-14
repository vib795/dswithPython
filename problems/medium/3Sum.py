'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = []
Output: []

Example 3:
Input: nums = [0]
Output: []
'''

class ThreeSum:
    def __init__(self, arr):
        self.arr = arr
        self.result = []

    def findThreeSum(self):
        found = False
        l = []
        for i in range(len(self.arr)-1): 
            # Find all pairs with sum  
            # equals to "-arr[i]"  
            s = set() 
            for j in range(i + 1, len(self.arr)): 
                x = -(self.arr[i] + self.arr[j]) 
                if x in s:
                    l+= [[x, self.arr[i], self.arr[j]]]
                    found = True
                else: 
                    s.add(self.arr[j]) 
        if found == False: 
            return []
        else:
            new_l = list(set(tuple(sorted(sub)) for sub in l))
            return [list(i) for i in new_l]


obj1 = ThreeSum([-1,0,1,2,-1,-4])
obj2 = ThreeSum([])
obj3 = ThreeSum([0])

print(obj1.findThreeSum())
print(obj2.findThreeSum())
print(obj3.findThreeSum())