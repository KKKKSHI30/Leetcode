# Trie
# Time: insert, sum: O(k)
# Space: insert, sum: O(k)
# 2023.07.17: yes
from matplotlib import collections

class TrieNode:
    def __init__(self):
        self.val = 0
        self.passby = 0
        self.children = {}

class MapSum(object):
    def __init__(self):
        self.root = TrieNode()
        self.map = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        if key in self.map:
            ori_val = self.map[key]
        node = self.root
        for i in key:
            if i not in node.children:
                node.children[i] = TrieNode()
                node.children[i].passby = val
            else:
                if key in self.map:
                    node.children[i].passby += (val - ori_val)
                else:
                    node.children[i].passby += val
            node = node.children[i]
        node.val = val
        self.map[key] = val

    def sum(self, prefix):
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

# Brute Force
# Time: insert, sum: O(1)
# Space: insert, sum: O(n)
# 2023.07.17: no
# notes:可以但是没必要
class MapSum2(object):
    def __init__(self):
        self.map = {}

    def insert(self, key, val):
        self.map[key] = val

    def sum(self, prefix):
        return sum(val for key, val in self.map.items()
                   if key.startswith(prefix))

# Prefix Hashmap
# Time: insert: O(k^2), sum: O(1)
# Space: insert: O(k^2), sum: O(1)
# 2023.07.17: no
# notes: 可以但是没必要
class MapSum3(object):
    def __init__(self):
        self.map = {}
        self.score = collections.Counter()

    def insert(self, key, val):
        delta = val - self.map.get(key, 0)
        self.map[key] = val
        for i in range(len(key) + 1):
            prefix = key[:i]
            self.score[prefix] += delta

    def sum(self, prefix):
        return self.score[prefix]

# Tests:
test = MapSum()
test.insert("apple", 3)
test.sum("ap")
test.insert("app", 2)
test.sum("ap")
test.insert("apple", 5)
test.sum("ap")