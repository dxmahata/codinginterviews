"""
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing 
only letters a-z or .. A . means it can represent any one letter.

For example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.
"""

class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = {}
        self.is_leaf = False
        
class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = TrieNode()
        
    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        current = self.root
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
        current.is_leaf = True
 
    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.dfs_search(self.root.children, word, 0)
        
    def dfs_search(self, children, word, start):
        
        if len(word) == start:
            if len(children) == 0:
                return True
            else:
                return False
                
        c = word[start]
        if c in children:
            if ((len(word)-1 == start) and (children[c].is_leaf)):
                return True
            return self.dfs_search(children[c].children, word, start + 1)
        elif c == ".":
            result = False
            for child in children:
                child_node = children[child]
                if ((len(word)-1 == start) and (child_node.is_leaf)):
                    return True
                if self.dfs_search(child_node.children, word, start+1):
                    result = True
            return result
        else:
            return False
                
if __name__ == "__main__":
    #Your WordDictionary object will be instantiated and called as such:
    wordDictionary = WordDictionary()
    wordDictionary.addWord("cat")
    wordDictionary.addWord("mat")
    wordDictionary.addWord("sat")
    wordDictionary.addWord("cataract")
    wordDictionary.addWord("saturday")
    
    print(wordDictionary.search("cat"))
    print(wordDictionary.search(".at"))
    print(wordDictionary.search("..t"))
    print(wordDictionary.search("c.."))
    print(wordDictionary.search("s.."))
    print(wordDictionary.search("c."))
    