# Top-Down Dynamic Programming
# Time: O(n^2+2^n+w)
# Space: O(2^n*n+w)
# 2023.07.24: no
# notes: 本质还是回溯，只是用一个表记下来了每一个节点他们后面的词有什么，到时候拼起来
from collections import defaultdict, Counter


class Solution:
    def wordBreak(self, s, wordDict):
        wordSet = set(wordDict)
        # table to map a string to its corresponding words break
        # {string: [['word1', 'word2'...], ['word3', 'word4', ...]]}
        memo = defaultdict(list)
        def _wordBreak_topdown(s):
            """ return list of word lists """
            if not s:
                return [[]]  # list of empty list

            if s in memo:
                # returned the cached solution directly.
                return memo[s]

            for endIndex in range(1, len(s)+1):
                word = s[:endIndex]
                if word in wordSet:
                    # move forwards to break the postfix into words
                    for subsentence in _wordBreak_topdown(s[endIndex:]):
                        memo[s].append([word] + subsentence)
            return memo[s]

        # break the input string into lists of words list
        _wordBreak_topdown(s)

        # chain up the lists of words into sentences.
        return [" ".join(words) for words in memo[s]]


# Bottom-Up Dynamic Programming
# Time: O(n^2+2^n+w)
# Space: O(2^n*n+w)
# 2023.07.24: no
# notes: 好理解的多的方法dp[i]记录打这个节点为止的目前形成的可能性，到0为止""， base case, 到n为止的时候
# 也是从0开始，subsentence就要加上0的""，如果是从4开始，就加上4现有的句子，比如"cats"，7的时候开始，就加"cat sand"
# 在更新dp的时候，已经是形成句子的状态，非常好理解
class Solution2:
    def wordBreak(self, s, wordDict):
        # quick check on the characters,
        #   otherwise it would exceed the time limit for certain test cases.
        if set(Counter(s).keys()) > set(Counter("".join(wordDict)).keys()):
            return []
        wordSet = set(wordDict)
        dp = [[]] * (len(s)+1)
        dp[0] = [""]
        for endIndex in range(1, len(s)+1):
            sublist = []
            # fill up the values in the dp array.
            for startIndex in range(0, endIndex):
                word = s[startIndex:endIndex]
                if word in wordSet:
                    for subsentence in dp[startIndex]:
                        sublist.append((subsentence + ' ' + word).strip())
            dp[endIndex] = sublist
        return dp[len(s)]

# Tests:
test = Solution2()
test.wordBreak(s="catsanddogo", wordDict=["cat", "cats", "and", "sand", "dog", "do", "go"])


# Backtracking
# Time: O(n^2+2^n+w)
# Space: O(2^n*n+w)
# 2023.07.24: no
# notes: 不是，为什么这道题的标答没有backtracking,顶中顶好吗，这道题就应该用backtrack解（不是），但是真的是最简单的暴力递归
class Solution3:
    def __init__(self):
        # 记录结果
        self.res = []
        # 记录回溯算法的路径
        self.track = []
        self.wordDict = []

    # 主函数
    def wordBreak(self, s, wordDict):
        self.wordDict = wordDict
        # 执行回溯算法穷举所有可能的组合
        self.backtrack(s, 0)
        return self.res

    # 回溯算法框架
    def backtrack(self, s: str, i: int) -> None:
        # base case
        if i == len(s):
            # 找到一个合法组合拼出整个 s，转化成字符串
            self.res.append(' '.join(self.track))
            return

        # 回溯算法框架
        for word in self.wordDict:
            # 看看哪个单词能够匹配 s[i..] 的前缀
            length = len(word)
            if i + length <= len(s) and s[i:i + length] == word:
                # 找到一个单词匹配 s[i..i+len)
                # 做选择
                self.track.append(word)
                # 进入回溯树的下一层，继续匹配 s[i+len..]
                self.backtrack(s, i + length)
                # 撤销选择
                self.track.pop()
