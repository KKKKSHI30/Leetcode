# Dynamic Programming 2D recursion
# Time: O(mn)
# Space: O(mn)
# 2023.07.26: yes
class Solution:
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])
        # 构造备忘录，初始值全部设为 -1
        memo = [[-1 for _ in range(n)] for _ in range(m)]

        def dp(i, j):
            # base case
            if i == 0 and j == 0:
                return grid[0][0]
            if i < 0 or j < 0:
                return float('inf')
            # 避免重复计算
            if memo[i][j] != -1:
                return memo[i][j]
            # 将计算结果记入备忘录
            memo[i][j] = min(
                dp(i - 1, j),
                dp(i, j - 1)
            ) + grid[i][j]

            return memo[i][j]

        return dp(m - 1, n - 1)

# Dynamic Programming 2D iteration
# Time: O(mn)
# Space: O(mn)
# 2023.07.26: yes
class Solution2(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[m-1][n-1]

# Dynamic Programming 1D Iteration
# Time: O(mn)
# Space: O(min(m,n))
# 2023.07.26: yes
class Solution3(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        dp = [0 for _ in range(n)]
        dp[0] = grid[0][0]
        for j in range(1, n):
            dp[j] = dp[j-1] + grid[0][j]
        for i in range(1, m):
            for j in range(n):
                if j == 0:
                    dp[j] = dp[j] + grid[i][j]
                else:
                    dp[j] = min(dp[j], dp[j-1]) + grid[i][j]
        return dp[n-1]

# Dynamic Programming No extra space
# Time: O(mn)
# Space: O(1)
# 2023.07.26: yes
# notes: 直接在grid上面改，但是有人说不好哈哈
class Solution4(object):
    def minPathSum(self, grid):
        rows, cols = len(grid), len(grid[0])
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                if i == rows - 1 and j != cols - 1:
                    grid[i][j] += grid[i][j + 1]
                elif j == cols - 1 and i != rows - 1:
                    grid[i][j] += grid[i + 1][j]
                elif i != rows - 1 and j != cols - 1:
                    grid[i][j] += min(grid[i + 1][j], grid[i][j + 1])
        return grid[0][0]


# Tests:
test = Solution3()
test.minPathSum(grid = [[1,2,3],[4,5,6]])
test.minPathSum(grid = [[1,3,1],[1,5,1],[4,2,1]])



















