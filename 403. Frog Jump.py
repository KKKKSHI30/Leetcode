# Hash map
# Time: O(n^2)
# Space: O(n^2)
# 2023.08.20: no
# notes: 自我感觉比标答好啊哈哈哈哈哈哈哈，大家的答案里也有这种解法
class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        if 1 not in stones:
            return False
        possibles = {key: set() for key in stones}
        possibles[1].add(1)
        for i in range(len(stones)):
            for j in possibles[stones[i]]:
                if stones[i] + j - 1 in stones and j - 1 > 0:
                    possibles[stones[i] + j - 1].add(j - 1)
                if stones[i] + j in stones:
                    possibles[stones[i] + j].add(j)
                if stones[i] + j + 1 in stones:
                    possibles[stones[i] + j + 1].add(j + 1)
        return len(possibles[stones[-1]]) != 0

# Dynamic Programming
# Time: O(n^2)
# Space: O(n^2)
# 2023.08.20: no
# notes: 用一个table记录T/F，无特别
class Solution2:
    def canCross(self, stones):
        mark = {}  # Dictionary to store stone positions and indices
        n = len(stones)
        dp = [[False] * 10 for _ in range(10)]  # 2D DP array

        for i in range(n):
            mark[stones[i]] = i

        dp[0][0] = True
        for index in range(n):
            for prevJump in range(n + 1):
                if dp[index][prevJump]:
                    if stones[index] + prevJump in mark:
                        dp[mark[stones[index] + prevJump]][prevJump] = True
                    if stones[index] + prevJump + 1 in mark:
                        dp[mark[stones[index] + prevJump + 1]][prevJump + 1] = True
                    if prevJump > 0 and stones[index] + prevJump - 1 in mark:
                        dp[mark[stones[index] + prevJump - 1]][prevJump - 1] = True

        for index in range(n + 1):
            if dp[n - 1][index]:
                return True

        return False


# Tests:
test = Solution2()
test.canCross([0, 1, 2, 3, 4, 8, 9, 11])
test.canCross([0, 1, 3, 5, 6, 8, 12, 17])
