'''
Given a string, determine if a permutation of the string could form a palindrome.

For example,
"code" -> False, "aab" -> True, "carerac" -> True

URL: https://leetcode.com/problems/palindrome-permutation/
'''
class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        else:
            palindrome_dict = {}
            for entries in s:
                if entries in palindrome_dict:
                    palindrome_dict[entries] += 1
                else:
                    palindrome_dict[entries] = 1
                
            no_odd_chars = 0
            for entries in palindrome_dict.values():
                if entries%2 != 0:
                    no_odd_chars += 1
                
            if len(s)%2 == 0:
                if no_odd_chars == 0:
                    return True
                else:
                    return False
            else:
                if no_odd_chars == 1:
                    return True
                else:
                    return False