'''
Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

Example 4:
Input: x = 0
Output: 0
'''

class ReverseInteger:
    def __init__(self, number):
        self.number = str(number)
        self.sign = ''
        self.afterSplit = []
        self.reversedNum = []
    
    def reverseInteger(self):
        self.afterSplit = [char for char in self.number]
        # Check if the input contains letters form the alphabet.
        for i in self.afterSplit:
            if i.isalpha():
                return "The number contains letters from the alphabet. Input a number."
        # Check if the number is signed.
        if self.afterSplit[0] in ['+', '-']:
            self.sign = self.afterSplit.pop(0)
        # Reverse the number. 
        self.afterSplit.reverse()
        if self.afterSplit[0] == 0:
            self.afterSplit.pop(0)
        if self.sign == '-':
            return int(self.sign + "".join(self.afterSplit))
        else:
            return int("".join(self.afterSplit))
        
obj = ReverseInteger(+321)
(print(obj.reverseInteger()))