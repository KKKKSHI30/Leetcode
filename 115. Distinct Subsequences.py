# Recursion + Memoization
# Time: O(nlogn)
# Space: O(n)
# 2023.06.21: no
# notes: -- 定义：s[i..] 的子序列中 t[j..] 出现的次数为 dp(s, i, t, j)
# dp(s, i, t, j) = SUM( dp(s, k + 1, t, j + 1) where k >= i and s[k] == t[j] )
# 对于所有的s[i] = t[j]都加起来，在之后去找，recursion
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = [[-1 for _ in range(len(t))] for _ in range(len(s))]

        def dp(i: int, j: int) -> int:
            # base case 1
            if j == len(t):
                return 1
            # base case 2
            if len(s) - i < len(t) - j:
                return 0
            # 查备忘录防止冗余计算
            if memo[i][j] != -1:
                return memo[i][j]
            res = 0
            # 执行状态转移方程
            # 在 s[i..] 中寻找 k，使得 s[k] == t[j]
            for k in range(i, len(s)):
                if s[k] == t[j]:
                    # 累加结果
                    res += dp(k + 1, j + 1)
            # 存入备忘录
            memo[i][j] = res
            return res

        return dp(0, 0)

# Recursion + Memoization
# Time: O(mn)
# Space: O(mn)
# 2023.06.21: no
# 定义：s[i..] 的子序列中 t[j..] 出现的次数为 dp(s, i, t, j)
# notes: iteration的方法，这个s[i]可以现在匹配t[j]也可以之后匹配，把两个情况加起来, Recursion
# func(i, j) = func(i + 1, j) + func(i + 1, j + 1) if char matches
# func(i, j) = func(i + 1, j) if char doesn't matches
class Solution2:
    def numDistinct(self, s: str, t: str) -> int:

        # Dictionary for memoization
        memo = {}

        def uniqueSubsequences(i, j):

            M, N = len(s), len(t)

            # Base case
            if i == M or j == N or M - i < N - j:
                return int(j == len(t))

            # Check if the result is already cached
            if (i, j) in memo:
                return memo[i, j]

            # Always make this recursive call
            ans = uniqueSubsequences(i + 1, j)

            # If the characters match, make the other
            # one and add the result to "ans"
            if s[i] == t[j]:
                ans += uniqueSubsequences(i + 1, j + 1)

            # Cache the answer and return
            memo[i, j] = ans
            return ans

        return uniqueSubsequences(0, 0)

# Iterative Dynamic Programming
# Time: O(mn)
# Space: O(mn)
# 2023.06.21: no
# notes: Iterative的方法，大概明白意思，但是看的云里雾里
# 可以重新看lc标答: https://leetcode.com/problems/distinct-subsequences/editorial/
# recurse(i, j) represents the number of distinct subsequences in string s[i⋯M]
# that equals the string t[j⋯N]
class Solution3:
    def numDistinct(self, s, t):

        M, N = len(s), len(t)

        # Dynamic Programming table
        dp = [[0 for i in range(N + 1)] for j in range(M + 1)]

        # Base case initialization
        for j in range(N + 1):
            dp[M][j] = 0

        # Base case initialization
        for i in range(M + 1):
            dp[i][N] = 1

        # Iterate over the strings in reverse so as to
        # satisfy the way we've modeled our recursive solution
        for i in range(M - 1, -1, -1):
            for j in range(N - 1, -1, -1):

                # Remember, we always need this result
                dp[i][j] = dp[i + 1][j]

                # If the characters match, we add the
                # result of the next recursion call (in this
                # case, the value of a cell in the dp table
                if s[i] == t[j]:
                    dp[i][j] += dp[i + 1][j + 1]

        return dp[0][0]

# Space optimized Dynamic Programming
# Time: O(mn)
# Space: O(n)
# 2023.06.21: no
# notes: 根据上一步，优化空间，因为其实只需要用到两行，下一行和当前行
class Solution4:
    def numDistinct(self, s: str, t: str) -> int:

        M, N = len(s), len(t)

        # Dynamic Programming table
        dp = [0 for j in range(N)]

        # Iterate over the strings in reverse so as to
        # satisfy the way we've modeled our recursive solution
        for i in range(M - 1, -1, -1):

            # At each step we start with the last value in
            # the row which is always 1. Notice how we are
            # starting the loop from N - 1 instead of N like
            # in the previous solution.
            prev = 1

            for j in range(N - 1, -1, -1):

                # Record the current value in this cell so that
                # we can use it to calculate the value of dp[j - 1]
                old_dpj = dp[j]

                # If the characters match, we add the
                # result of the next recursion call (in this
                # case, the value of a cell in the dp table
                if s[i] == t[j]:
                    dp[j] += prev

                # Update the prev variable
                prev = old_dpj

        return dp[0]

# test:
test = Solution3()
test.numDistinct(s = "rabbbita", t = "rabbit")
