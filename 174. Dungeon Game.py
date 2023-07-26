# Dynamic Programming 2D recursion
# Time: O(mn)
# Space: O(mn)
# 2023.07.26: no
# notes: 不能从(0,0)开始推，但是可以从(m-1)(n-1)开始推
class Solution:
    def calculateMinimumHP(self, grid):
        m = len(grid)
        n = len(grid[0])
        # 备忘录中都初始化为 -1
        memo = [[-1 for _ in range(n)] for _ in range(m)]

        return self.dp(grid, 0, 0, memo)

    # 备忘录，消除重叠子问题
    def dp(self, grid, i, j, memo):
        m = len(grid)
        n = len(grid[0])
        # base case
        if i == m - 1 and j == n - 1:
            return 1 if grid[i][j] >= 0 else -grid[i][j] + 1
        if i == m or j == n:
            return float('inf')
        # 避免重复计算
        if memo[i][j] != -1:
            return memo[i][j]
        # 状态转移逻辑
        res = min(
                self.dp(grid, i, j + 1, memo),
                self.dp(grid, i + 1, j, memo)
            ) - grid[i][j]
        # 骑士的生命值至少为 1
        memo[i][j] = 1 if res <= 0 else res

        return memo[i][j]


# Dynamic Programming 2D Iteration
# Time: O(mn)
# Space: O(mn)
# 2023.07.26: yes
# notes: 状态转移方程和recursion一样，必须从(m-1)(n-1)倒着推
class Solution2:
    def calculateMinimumHP(self, dungeon):
        m, n = len(dungeon), len(dungeon[0])
        dp = [[float("inf")] * (n + 1) for _ in range(m + 1)]
        dp[m - 1][n], dp[m][n - 1] = 1, 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[i][j] = max(min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j], 1)
        return dp[0][0]


# Binary Search
# Time: O(mn)
# Space: O(mn)
# 2023.07.26: no
# notes: BS的一种思路，假定骑士的血量是1，1000中间，不断二分，非标答
class Solution3:
    def calculateMinimumHP(self, grid):
        m, n = len(grid), len(grid[0])

        def isGood(initHealth):
            dp = [[0] * n for _ in range(m)]
            dp[0][0] = initHealth + grid[0][0]
            for r in range(m):
                for c in range(n):
                    if r > 0 and dp[r - 1][c] > 0:
                        dp[r][c] = max(dp[r][c], dp[r - 1][c] + grid[r][c])
                    if c > 0 and dp[r][c - 1] > 0:
                        dp[r][c] = max(dp[r][c], dp[r][c - 1] + grid[r][c])
            return dp[m - 1][n - 1] > 0

        left = 1
        right = 1000 * (m + n) + 1
        ans = right
        while left <= right:
            mid = left + (right - left) // 2
            if isGood(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans

# Dynamic Programming with Circular Queue
# Time: O(mn)
# Space: O(mn)
# 2023.07.26: no
# notes: recursion的O(n)省空间方法，利用一个array去存储，是circular，但是我觉得直接替换也行，之后再看
class MyCircularQueue:
    def __init__(self, capacity):
        """
        Set the size of the queue to be k.
        """
        self.queue = [0]*capacity
        self.tailIndex = 0
        self.capacity = capacity

    def enQueue(self, value):
        """
        Insert an element into the circular queue.
        """
        self.queue[self.tailIndex] = value
        self.tailIndex = (self.tailIndex + 1) % self.capacity

    def get(self, index):
        return self.queue[index % self.capacity]


class Solution4(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        rows, cols = len(dungeon), len(dungeon[0])
        # Use a circular queue to keep a sliding window of DP values
        dp = MyCircularQueue(cols)

        def get_min_health(currCell, nextRow, nextCol):
            if nextRow < 0 or nextCol < 0:
                return float('inf')
            index = cols * nextRow + nextCol
            nextCell = dp.get(index)
            # hero needs at least 1 point to survive
            return max(1, nextCell - currCell)

        for row in range(rows):
            for col in range(cols):
                # iterate the grid in the reversed order
                currCell = dungeon[rows-row-1][cols-col-1]

                right_health = get_min_health(currCell, row, col-1)
                down_health = get_min_health(currCell, row-1, col)
                next_health = min(right_health, down_health)

                if next_health != float('inf'):
                    min_health = next_health
                else:
                    min_health = 1 if currCell >= 0 else (1 - currCell)

                dp.enQueue(min_health)
        # return the last element in the queue
        return dp.get(cols-1)

# Tests:
test = Solution4()
test.calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]])

# Dynamic Programming with O(a) space
# Time: O(mn)
# Space: O(1)
# 2023.07.26: no
# notes: 与之前的题类似，直接在原dungeon上面进行更改，可以实现O(1)空间
class Solution5(object):
    def calculateMinimumHP(self, dungeon):
        m, n = len(dungeon), len(dungeon[0])
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    dungeon[i][j] = min(dungeon[i][j], 0) * -1 + 1
                elif i == m - 1:
                    dungeon[i][j] = max(dungeon[i][j + 1] - dungeon[i][j], 1)
                elif j == n - 1:
                    dungeon[i][j] = max(dungeon[i + 1][j] - dungeon[i][j], 1)
                else:
                    dungeon[i][j] = max(min(dungeon[i][j + 1], dungeon[i + 1][j]) - dungeon[i][j], 1)
        return dungeon[0][0]