# Trie + Depth-First Search [Accepted]
# Time: O(sigma wi)
# Space: O(sigma wi)
# 2023.08.28: no
# notes: 两步，第一步insert，第二步遍历检查，只不过insert的方法很巧妙，排除了我一个个insert，考虑Node是不是空的情况
# 也是可以做的，但是这道题不能按照length来排序做，更贴合Trie的性质一点
import collections

class TrieNode(object):
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isEnd = False
        self.word = ""

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            node = node.children[c]
        node.isEnd = True
        node.word = word

    def bfs(self):
        q = collections.deque([self.root])
        res = ""
        while q:
            cur = q.popleft()
            for n in cur.children.values():
                if n.isEnd:
                    q.append(n)
                    if len(n.word) > len(res) or n.word < res:
                        res = n.word
        return res

class Solution(object):
    def longestWord(self, words):
        trie = Trie()
        for w in words:
            trie.insert(w)
        return trie.bfs()


# Tests:
test = Solution()
test.longestWord(["w", "wo", "wor", "worl", "world"])
