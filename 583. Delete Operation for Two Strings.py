# Without using LCS Dynamic Programmming
# Time: O(mn)
# Space: O(mn)
# 2023.07.25: yes
# notes: 注意base case，和矩阵大小
class Solution:
    def minDistance(self, word1, word2):
        m, n = len(word1), len(word2)
        dp = [[0 for _ in range(n+1)]  for _ in range(m+1)]
        for i in (range(m+1)):
            for j in (range(n+1)):
                if i == 0 or j == 0:
                    dp[i][j] = i+j
                elif word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1])+1
        return dp[m][n]

# Longest Common Subsequence with Memoization
# Time: O(mn)
# Space: O(mn)
# 2023.07.25: yes
# notes: 最长公共自序列，就是1143题
class Solution2:
    def minDistance(self,s1, s2):
        memo = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        return len(s1) + len(s2) - 2 * self.lcs(s1, s2, len(s1), len(s2), memo)

    def lcs(self, s1, s2, m, n, memo):
        if m == 0 or n == 0:
            return 0
        if memo[m][n] > 0:
            return memo[m][n]
        if s1[m - 1] == s2[n - 1]:
            memo[m][n] = 1 + self.lcs(s1, s2, m - 1, n - 1, memo)
        else:
            memo[m][n] = max(self.lcs(s1, s2, m, n - 1, memo), self.lcs(s1, s2, m - 1, n, memo))
        return memo[m][n]

# Using Longest Common Subsequence- Dynamic Programming
# Time: O(mn)
# Space: O(mn)
# 2023.07.25: yes
class Solution3:
    def minDistance(self, s1, s2):
        dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i == 0 or j == 0:
                    continue
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return len(s1) + len(s2) - 2 * dp[len(s1)][len(s2)]

# 1-D Dynamic Programming
# Time: O(mn)
# Space: O(n)
# 2023.07.25: no
# notes: 记录上一行的数据即可
class Solution4:
    def minDistance(self, s1, s2):
        dp = [0] * (len(s2) + 1)
        for i in range(len(s1) + 1):
            temp = [0] * (len(s2) + 1)
            for j in range(len(s2) + 1):
                if i == 0 or j == 0:
                    temp[j] = i + j
                elif s1[i - 1] == s2[j - 1]:
                    temp[j] = dp[j - 1]
                else:
                    temp[j] = 1 + min(dp[j], temp[j - 1])
            dp = temp
        return dp[len(s2)]



# Tests:
test = Solution()
test.minDistance(word1 = "leetcode", word2 = "etco")
test.minDistance(word1 = "sea", word2 = "eat")


