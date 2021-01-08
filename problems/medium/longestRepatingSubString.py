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

# Python3 program to find the length 
# of the longest substrring without 
# repeating characters 
  
# This functionr eturns true if all 
# characters in strr[i..j] are  
# distinct, otherwise returns false 
def areDistinct(strr, i, j): 
  
    # Note : Default values in visited are false 
    visited = [0] * (26) 
  
    for k in range(i, j + 1): 
        if (visited[ord(strr[k]) - 
                   ord('a')] == True): 
            return False
              
        visited[ord(strr[k]) -
                ord('a')] = True
  
    return True
  
# Returns length of the longest substrring 
# with all distinct characters. 
def longestUniqueSubsttr(strr): 
      
    n = len(strr) 
      
    # Result 
    res = 0 
      
    for i in range(n): 
        for j in range(i, n): 
            if (areDistinct(strr, i, j)): 
                res = max(res, j - i + 1) 
                  
    return res 
  
# Driver code 
if __name__ == '__main__': 
      
    strr = "abcabcbb"
    print("The input is ", strr) 
      
    len = longestUniqueSubsttr(strr) 
    print("The length of the longest "
          "non-repeating character substring is ", len)