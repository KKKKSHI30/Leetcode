from collections import Counter

class Solution(object):
    def checkAlmostEquivalent(self, s, t):
        result = []
        for i in range(len(s)):
            word1, word2 = s[i], t[i]
            if all(v < 4 for v in ((Counter(word1) - Counter(word2)) + (Counter(word2) - Counter(word1))).values()):
                result.append("Yes")
            else:
                result.append("No")
        return result

# Tests:
test = Solution()
test.checkAlmostEquivalent(s = ['aabaab', 'aaaaabb'], t = ['bbabbc', 'abb'])