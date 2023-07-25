# Trie
# Time: insert, search, search_prefix: O(m)
# Space: insert: O(m), search, search_prefix: O(1)
# 2023.07.16: yes

class TrieNode:
    def __init__(self):
        self.val = False
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
            node = node.children[i]
        node.val = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        node = self.root
        for i in word:
            if i not in node.children:
                return False
            node = node.children[i]
        return node.val

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for i in prefix:
            if i not in node.children:
                return False
            node = node.children[i]
        return True

# Tests:
obj = Trie()
obj.insert("apple")
obj.startsWith("app")
obj.search("apple")
obj.startsWith("apple")
