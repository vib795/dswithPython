'''
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Example 4:
Input: s = ""
Output: 0
'''

class LongestRepeatingSubString:
    def __init__(self, s):
        self.s  = str(s)
        self.afterSplit = ''

    def check(self):
        l = []
        self.afterSplit = [char for char in self.s]
        # for c in self.afterSplit:
        #     print(c)
        for i in range(len(0, self.afterSplit)):
            if l[-1] != self.afterSplit[i]:
                l.append(self.afterSplit.pop(i))

obj = LongestRepeatingSubString('abcabcbb')
obj.check()