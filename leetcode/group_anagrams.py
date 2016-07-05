"""
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]

URL: https://leetcode.com/problems/anagrams/
"""
from collections import defaultdict
class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        anagram_dict = defaultdict(list)
        for entries in strs:
            sorted_str = "".join(sorted(entries))
            anagram_dict[sorted_str].append(entries)
            
        return [entries for entries in anagram_dict.values()]
    
if __name__ == "__main__":
    soln = Solution()
    print(soln.anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
        