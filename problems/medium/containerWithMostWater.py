'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, 
together with the x-axis forms a container, such that the container contains the most water.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Example 3:
Input: height = [4,3,2,1,4]
Output: 16

Example 4:
Input: height = [1,2,1]
Output: 2
'''

class ContainerWithMostWater:
    def __init__(self, heightArray):
        self.heightArray = heightArray
        self.maxArea = 0

    def calculateArea(self):
        for i in range(1, len(self.heightArray)):
            if self.maxArea < i * self.heightArray[i]:
                self.maxArea = i * self.heightArray[i]
        return self.maxArea

obj = ContainerWithMostWater([1,8,6,2,5,4,8,3,7])
print(obj.calculateArea())