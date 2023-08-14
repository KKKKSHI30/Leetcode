# Breadth-First Search
# Time: O(n^3 + mk)
# Space: O(n+m*k)
# 2023.07.22: yes
# notes: 从每一个start开始检查，end检查，把见过的放到queue里，弹出的时候就是start的位置
from collections import deque
from functools import cache
class Solution:
    def wordBreak(self, s, wordDict):
        words = set(wordDict)
        queue = deque([0])
        seen = set()

        while queue:
            start = queue.popleft()
            if start == len(s):
                return True

            for end in range(start + 1, len(s) + 1):
                if end in seen:
                    continue

                if s[start:end] in words:
                    queue.append(end)
                    seen.add(end)
        return False

# Top-Down Dynamic Programming
# Time: O(nmk)
# Space: O(n)
# 2023.07.22: no
# notes: 利用递归的方法，从i = len(n)-1开始，匹配一个单词，符合的话i = i-len(word)+1，说明进入下一层递归
class Solution2:
    def wordBreak(self, s, wordDict) :
        @cache
        def dp(i):
            if i < 0:
                return True
            for word in wordDict:
                if s[i - len(word) + 1:i + 1] == word and dp(i - len(word)):
                    return True
            return False
        return dp(len(s) - 1)

# Bottom-Up Dynamic Programming
# Time: O(nmk)
# Space: O(n)
# 2023.07.22: no
# notes: 用dp的方法，根据dp[i]是到i为止，这个点之前是不是True，从i = 0到i = len(s) -1开始循环
# 标记True有两个情况，第一，这个词很长，直接覆盖这个点，第二，这个词从上个i = True出发，是True，也就是接下去
# 上一个方法用了cache，这个是用array的方式存储结果
class Solution3:
    def wordBreak(self, s, wordDict):
        dp = [False] * len(s)
        for i in range(len(s)):
            for word in wordDict:
                # Handle out of bounds case
                if i < len(word) - 1:
                    continue
                if i == len(word) - 1 or dp[i - len(word)]:
                    if s[i - len(word) + 1:i + 1] == word:
                        dp[i] = True
                        break
        return dp[-1]

# Trie Optimization
# Time: O(n^2+mk)
# Space: O(n+mk)
# 2023.07.22: no
# notes: 利用trienode加速进度，是单词的标记为True，下次只从true的下一个开始当rootnode查询有没有子节点，和上一题差不多，只是
# 确认True的过程加速
class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}

class Solution4:
    def wordBreak(self, s, wordDict):
        root = TrieNode()
        for word in wordDict:
            curr = root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.is_word = True
        dp = [False] * len(s)
        for i in range(len(s)):
            if i == 0 or dp[i - 1]:
                curr = root
                for j in range(i, len(s)):
                    c = s[j]
                    if c not in curr.children:
                        # No words exist
                        break
                    curr = curr.children[c]
                    if curr.is_word:
                        dp[j] = True
        return dp[-1]


# Backtracking (time exceed)
# notes: 只是用来比较backtracking与dp的区别，超时
from typing import List

class Solution4:
    def __init__(self):
        self.wordDict = []
        # 记录是否找到一个合法的答案
        self.found = False
        # 记录回溯算法的路径
        self.track = []

    # 主函数
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.wordDict = wordDict
        # 执行回溯算法穷举所有可能的组合
        self.backtrack(s, 0)
        return self.found

    # 回溯算法框架
    def backtrack(self, s: str, i: int):
        # base case
        if self.found:
            # 如果已经找到答案，就不要再递归搜索了
            return
        if i == len(s):
            # 整个 s 都被匹配完成，找到一个合法答案
            self.found = True
            return

        # 回溯算法框架
        for word in self.wordDict:
            # 看看哪个单词能够匹配 s[i..] 的前缀
            length = len(word)
            if i + length <= len(s) and s[i:i+length] == word:
                # 找到一个单词匹配 s[i..i+length)
                # 做选择
                self.track.append(word)
                # 进入回溯树的下一层，继续匹配 s[i+length..]
                self.backtrack(s, i+length)
                # 撤销选择
                self.track.pop()



# Tests:
test = Solution4()
test.wordBreak(s = "catsandog", wordDict = ["cats","dog","sand","and","cat"])
test.wordBreak(s = "leetcode", wordDict = ["leet","code"])
