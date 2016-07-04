"""
Given a string s and a dictionary of words dict, determine if s can be segmented 
into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
"""
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        if len(s) == 0 or s == None:
            return True
        elif len(s) == 1 and s in wordDict:
            return True
        else:
            valid_words = [False]*len(s)
            n = len(s)
            for i in range(0, n):
                if s[0:i+1] in wordDict:
                    valid_words[i] = True
                if valid_words[i] == True and i == n - 1:
                    return True
                elif valid_words[i] == True and i < n - 1:
                    for j in range(i+1, n):
                        if s[i+1:j+1] in wordDict:
                            valid_words[j] = True
                        if j == n-1 and valid_words[j] == True:
                            return True
            return False
        
if __name__ == "__main__":
    s = "leetcode"
    wordDict = ["leet", "code"]
    soln = Solution()
    print(soln.wordBreak(s, wordDict))
    s = "apple"
    wordDict = ["pear","apple","peach"]
    print(soln.wordBreak(s, wordDict))
                            
            