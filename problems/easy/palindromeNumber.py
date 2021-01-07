'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
Follow up: Could you solve it without converting the integer to a string?

Example 1:
Input: x = 121
Output: true

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Example 4:
Input: x = -101
Output: false
'''

class PalindromeNumber:
    def __init__(self, number):
        self.number = number
        self.basepos = 1
        self.rev_num = 0

    def palindromeNumber(self, number):
        if(self.number > 0): 
            self.palindromeNumber((int)(self.number / 10)) 
            self.rev_num += (self.number % 10) * self.basepos 
            self.basepos *= 10
        return self.rev_num

obj1 = PalindromeNumber(121)
obj2 = PalindromeNumber(-121)
obj3 = PalindromeNumber(10)
obj4 = PalindromeNumber(-101)

obj1.palindromeNumber(121)
obj2.palindromeNumber(-121)
obj3.palindromeNumber(10)
obj4.palindromeNumber(-101)