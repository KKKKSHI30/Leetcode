# Trie
# Time: O(n)
# Space: O(n)
# 2023.07.16: yes
from functools import reduce
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.val = 0
        self.children = {}

class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        # create Trie
        start = 0
        self.root = TrieNode()
        for word in dictionary:
            node = self.root
            for i in word:
                if i not in node.children:
                    node.children[i] = TrieNode()
                node = node.children[i]
            start += 1
            node.val = start

        sentence = sentence.split()
        result = []
        for word in sentence:
            node = self.root
            for i in word:
                if node.val != 0:
                    break
                if i not in node.children:
                    break
                node = node.children[i]
            if node.val:
                result.append(dictionary[node.val-1])
            else:
                result.append(word)
        return " ".join(result)


class Solution2(object):
    def replaceWords(self, roots, sentence):
        Trie = lambda: defaultdict(Trie)
        trie = Trie()
        END = True

        for root in roots:
            reduce(dict.__getitem__, root, trie)[END] = root

        def replace(word):
            cur = trie
            for letter in word:
                if letter not in cur or END in cur: break
                cur = cur[letter]
            return cur.get(END, word)

        return " ".join(map(replace, sentence.split()))


# Prefix Hash
# Time: O(wi^2), wi is length of i-th word
# Space: O(n)
# 2023.07.16: yes
class Solution3(object):
    def replaceWords(self, roots, sentence):
        rootset = set(roots)

        def replace(word):
            for i in range(1, len(word)):
                if word[:i] in rootset:
                    return word[:i]
            return word

        return " ".join(map(replace, sentence.split()))

# Tests:
test = Solution2()
test.replaceWords(["cat","bat","rat"], "the cattle was rattled by the battery")
test.replaceWords(["a","b","c"], "aadsfasf absbs bbab cadsfafs")
test.replaceWords(["a", "aa", "aaa", "aaaa"], "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa")

