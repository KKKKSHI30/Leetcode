from collections import deque

class Solution:
    def wordBreak(self, s, wordDict):
        def wordBreakRecur(s: str, word_dict, start):
            if start == len(s):
                return True
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in word_dict and wordBreakRecur(s, word_dict, end):
                    return True
            return False
        return wordBreakRecur(s, set(wordDict), 0)


class Solution2:
    def wordBreak(self, s, wordDict):
        def wordBreakMemo(s, word_dict, start):
            if start == len(s):
                return True
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in word_dict and wordBreakMemo(s, word_dict, end):
                    return True
            return False
        return wordBreakMemo(s, frozenset(wordDict), 0)

class Solution3:
    def wordBreak(self, s: str, wordDict):
        word_set = set(wordDict)
        q = deque()
        visited = set()
        q.append(0)
        while q:
            start = q.popleft()
            if start in visited:
                continue
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in word_set:
                    q.append(end)
                    if end == len(s):
                        return True
            visited.add(start)
        return False

class Solution4:
    def wordBreak(self, s, wordDict):
        word_set = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[len(s)]
test = Solution4()
test.wordBreak("catsanddog",["cat", "cats","sand","and","dog"])
