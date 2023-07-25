# Memoization: Top-Down Dynamic Programming
# Time: O(mn)
# Space: O(mn)
# 2023.07.24: no
# notes: 这道题看着很难，其实可以拆分成4个动作，增改删不动
# 如果不动的话，s[i] = s[j], i和j都可以往前移动一格
# 如果s[i]需要增加一个到s[j]的话，j往前移动一格，i不变
# 如果s[i]需要删除一个到s[j]的话，i往前移动一格，j不变
# 如果s[i]需要替换一个到s[j]的话，i和j都往前移动一格，（斜向）
# dp的这个列表代表着到当前节点需要多少步
# base case就是如果一个字符走完了，需要移动的动作自然就是剩下那个字符查找到的进度的长度,+1是因为计算长度从0开始计算
class Solution:
    def __init__(self):
        self.memo = []

    def minDistance(self, s1, s2):
        m, n = len(s1), len(s2)
        # 备忘录初始化为特殊值，代表还未计算
        self.memo = [[-1] * n for _ in range(m)]
        return self.dp(s1, m - 1, s2, n - 1)

    def dp(self, s1, i, s2, j):
        # 当一个word已经走完了，剩下需要做的就是把另一个补全，因为是i = 0开始计数的，所以需要加1
        if i == -1:
            return j + 1
        if j == -1:
            return i + 1

        # 查备忘录，避免重叠子问题
        if self.memo[i][j] != -1:
            return self.memo[i][j]

        # 状态转移，结果存入备忘录
        if s1[i] == s2[j]:
            self.memo[i][j] = self.dp(s1, i - 1, s2, j - 1)
        else:
            self.memo[i][j] = min(
                self.dp(s1, i, s2, j - 1) + 1,
                self.dp(s1, i - 1, s2, j) + 1,
                self.dp(s1, i - 1, s2, j - 1) + 1
            )

        return self.memo[i][j]


# Memoization: Top-Down Dynamic Programming
# Time: O(mn)
# Space: O(mn)
# 2023.07.24: no
# notes: 基本思路和上面一样，重点是base case，dp[i][0] = i，就是如果一个字符走完了，剩下一个还需要多少步
class Solution2:
    def minDistance(self,s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        # 定义：s1[0..i] 和 s2[0..j] 的最小编辑距离是 dp[i+1][j+1]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # base case
        # If word1 is empty, the edit distance is equal to the length of word2.
        # If word2 is empty, the edit distance is equal to the length of word1.
        # 如果还是看不懂base case，标答讲的最好
        for i in range(1, m + 1):
            dp[i][0] = i
        for j in range(1, n + 1):
            dp[0][j] = j
        # 自底向上求解
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i - 1][j] + 1,
                        dp[i][j - 1] + 1,
                        dp[i - 1][j - 1] + 1
                    )
        # 储存着整个 s1 和 s2 的最小编辑距离
        return dp[m][n]

# Tests:
test = Solution()
test.minDistance("horse", "ros")