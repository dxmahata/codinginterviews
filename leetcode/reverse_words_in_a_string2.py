"""
Given an input string, reverse the string word by word. A word is defined as a sequence of non-space characters.

The input string does not contain leading or trailing spaces and the words are always separated by a single space.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Could you do it in-place without allocating extra space?

URL: https://leetcode.com/problems/reverse-words-in-a-string-ii/
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: a list of 1 length strings (List[str])
        :rtype: nothing
        """
        if s:
            i = 0
            for j in range(len(s)):
                if s[j] == " ":
                    self.reverse(s, i, j-1)
                    i = j + 1
            
            self.reverse(s, i, len(s) - 1)
            self.reverse(s, 0, len(s) - 1)
        
            
    def reverse(self, s_arr, i, j):
        while i < j:
            temp = s_arr[i]
            s_arr[i] = s_arr[j]
            s_arr[j] = temp
            i += 1
            j -= 1