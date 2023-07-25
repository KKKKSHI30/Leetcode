# Bottom-Up Dynamic Programming
# Time: O(nlogn)
# Space: O(n)
# 2023.06.21: yes
class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        row, col = len(matrix), len(matrix[0])
        dp = [[float("inf") for _ in range(col+2)] for _ in range(row)]
        for i in range(col):
            dp[0][i+1] = matrix[0][i]

        for i in range(1,row):
            for j in range(1, col+1):
                print(j, i)
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1]) + matrix[i][j-1]
        return min(dp[row-1])


# Top Down Dynamic Programming
# Time: O(n^2)
# Space: O(n^2)
# 2023.06.21: no
class Solution2:
    def minFallingPathSum(self, matrix):
        minFallingSum = float('inf')
        memo = [[None for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        # Start a DFS (with memoization) from each cell in the top row
        for startCol in range(len(matrix)):
            minFallingSum = min(minFallingSum,
                                self.findMinFallingPathSum(matrix, 0, startCol, memo))

        return minFallingSum

    def findMinFallingPathSum(self, matrix, row, col, memo):
        # Base cases
        if col < 0 or col == len(matrix[0]):
            return float('inf')

        # Check if we have reached the last row
        if row == len(matrix) - 1:
            return matrix[row][col]

        # Check if the results are calculated before
        if memo[row][col] is not None:
            return memo[row][col]

        # Calculate the minimum falling path sum starting from each possible next step
        left = self.findMinFallingPathSum(matrix, row + 1, col, memo)
        middle = self.findMinFallingPathSum(matrix, row + 1, col + 1, memo)
        right = self.findMinFallingPathSum(matrix, row + 1, col - 1, memo)

        memo[row][col] = min(left, middle, right) + matrix[row][col]
        return memo[row][col]



# Bottom-Up Dynamic Programming
# Time: O(n^2)
# Space: O(n^2)
# 2023.06.21: no
class Solution3:
    def minFallingPathSum(self, matrix):
        n = len(matrix)
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

        for row in range(n - 1, -1, -1):
            for col in range(n):
                if col == 0:
                    dp[row][col] = min(dp[row + 1][col], dp[row + 1][col + 1]) + matrix[row][col]
                elif col == n - 1:
                    dp[row][col] = min(dp[row + 1][col], dp[row + 1][col - 1]) + matrix[row][col]
                else:
                    dp[row][col] = min(dp[row + 1][col], dp[row + 1][col + 1], dp[row + 1][col - 1]) + matrix[row][col]

        minFallingSum = float('inf')
        for startCol in range(n):
            minFallingSum = min(minFallingSum, dp[0][startCol])

        return minFallingSum


# Space Optimized, Bottom-Up Dynamic Programming (best approach)
# Time: O(n^2)
# Space: O(n)
# 2023.06.21: no
# notes: 只需要记录下一行，和当前行即可
class Solution4:
    def minFallingPathSum(self, matrix):
        dp = [0] * (len(matrix[0]) + 1)
        for row in range(len(matrix) - 1, -1, -1):
            currentRow = [0] * (len(matrix[0]) + 1)
            for col in range(len(matrix)):
                if col == 0:
                    currentRow[col] = min(dp[col], dp[col + 1]) + matrix[row][col]
                elif col == len(matrix[0]) - 1:
                    currentRow[col] = min(dp[col], dp[col - 1]) + matrix[row][col]
                else:
                    currentRow[col] = min(dp[col], dp[col + 1], dp[col - 1]) + matrix[row][col]
            dp = currentRow
        minFallingSum = float('inf')
        for startCol in range(len(matrix)):
            minFallingSum = min(minFallingSum, dp[startCol])
        return minFallingSum




# Tests:
test = Solution4()
test.minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]])
test.minFallingPathSum([[-19,57],[-40,-5]])
