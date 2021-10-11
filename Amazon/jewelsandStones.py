'''
You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. 
Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3

Example 2:
Input: jewels = "z", stones = "ZZ"
Output: 0
'''

class Solution:
    def __init__(self, jewels, stones):
        self.jewels =   jewels
        self.stones =   stones

    def numJewelsInStones(self):
        finalcount = 0
        for i in list(self.stones):
            finalcount = finalcount + list(self.jewels).count(i)
        return finalcount

s1 = Solution(jewels = "aA", stones = "aAAbbbb")
print(s1.numJewelsInStones())

s2 = Solution(jewels = "z", stones = "ZZ")
print(s2.numJewelsInStones())