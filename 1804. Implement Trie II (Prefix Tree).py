# Trie
# Time: insert, search, search_prefix: O(m)
# Space: insert: O(m), search, search_prefix: O(1)
# 2023.07.16: yes
class TrieNode:
    def __init__(self):
        self.val = 0
        self.passby = 0
        self.children = {}

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i] = TrieNode()
                node.children[i].passby = 1
            else:
                node.children[i].passby += 1
            node = node.children[i]
        node.val += 1

    def countWordsEqualTo(self, word):
        """
        :type word: str
        :rtype: int
        """
        node = self.root
        for i in word:
            if i not in node.children:
                return 0
            node = node.children[i]
        return node.val

    def countWordsStartingWith(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        node = self.root
        for i in prefix:
            if i not in node.children:
                return 0
            node = node.children[i]
        return node.passby

    def erase(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        for i in word:
            node = node.children[i]
            node.passby -= 1
        node.val -= 1

# Tests:
obj3 = Trie()
obj3.countWordsEqualTo("w")
obj3.insert("w")
obj3.erase("w")
obj3.countWordsStartingWith("w")
obj3.insert("w")


obj2 = Trie()
obj2.insert("cu")
obj2.countWordsEqualTo("cu")
obj2.countWordsEqualTo("cu")
obj2.insert("cu")
obj2.countWordsStartingWith("c")
obj2.insert("cye")
obj2.countWordsStartingWith("c")
obj2.insert("cu")
obj2.countWordsStartingWith("c")
obj2.erase("cu")

obj = Trie()
obj.insert("apple")
obj.insert("apple")
obj.countWordsEqualTo("apple")
obj.countWordsStartingWith("app")
obj.erase("apple")
obj.countWordsEqualTo("apple")
obj.countWordsStartingWith("app")
obj.erase("apple")
obj.countWordsStartingWith("app")

