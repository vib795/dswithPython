'''
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Example 1:
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Example 2:
Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

Example 3:
Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
'''

class Solution:
    def __init__(self, nums):
        self.nums   =   nums

    def runningSum(self):
        runningSum = 0
        l = []        
        if len(self.nums) == 1:
            return "Running sum is: " + str(self.nums[0])
        if len(self.nums) == 0:
            return "Length of the passed array is 0. Are you kidding me?"
        if len(self.nums) >= 2:
            for i in range(len(self.nums)):
                if i == 0:
                    runningSum = self.nums[i]
                    l.append(runningSum)
                else:
                    runningSum = runningSum + self.nums[i]
                    l.append(runningSum)
        return l 

s1 = Solution([1,2,3,4])
print(s1.runningSum())

s2 = Solution([1,1,1,1,1])
print(s2.runningSum())

s3 = Solution([3,1,2,10,1])
print(s3.runningSum())