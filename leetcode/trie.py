"""
Implement a trie with insert, search, and startsWith methods.

Note:
You may assume that all inputs are consist of lowercase letters a-z.

URL: https://leetcode.com/problems/implement-trie-prefix-tree/
"""

class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = {}
        self.is_leaf = False
        

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
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
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current = self.root
        for c in word:
            if c not in current.children:
                return False
            current = current.children[c]
        return current.is_leaf
        
    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        current = self.root
        for c in prefix:
            if c not in current.children:
                return False
            current = current.children[c]
        return True
        
if __name__ == "__main__":
    # Your Trie object will be instantiated and called as such:
    trie = Trie()
    trie.insert("cat")
    trie.insert("mat")
    trie.insert("sat")
    trie.insert("cataract")
    trie.insert("saturday")
    
    print(trie.search("cat"))
    print(trie.search("cataract"))
    print(trie.search("saturday"))
    print(trie.search("target"))
    
    print(trie.startsWith("ca"))
    print(trie.startsWith("sa"))
    print(trie.startsWith("ta"))
    