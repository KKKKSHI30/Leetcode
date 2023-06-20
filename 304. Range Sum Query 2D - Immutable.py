# Caching Smarter Approach (best approach):
# Time: O(1)
# Space: O(mn)
# 2023.06.19: yes

class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        m, n = len(matrix), len(matrix[0])
        self.sum_matrix = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.sum_matrix[i][j] = self.sum_matrix[i - 1][j] + self.sum_matrix[i][j - 1] + matrix[i - 1][j - 1] - self.sum_matrix[i - 1][j - 1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.sum_matrix[row2 + 1][col2 + 1] - self.sum_matrix[row1][col2 + 1] - self.sum_matrix[row2 + 1][col1] + self.sum_matrix[row1][col1]

# Tests:
numMatrix = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
numMatrix.sumRegion(2, 1, 4, 3)
numMatrix.sumRegion(1, 1, 2, 2)
numMatrix.sumRegion(1, 2, 2, 4)
numMatrix.sumRegion(0, 1, 2, 2)
numMatrix.sumRegion(1, 0, 2, 2)
numMatrix2 = NumMatrix([[-1]])
numMatrix2.sumRegion(0,0,0,0)
numMatrix3 = NumMatrix([[-4,-5]])
numMatrix3.sumRegion(0,0,0,0)
numMatrix3.sumRegion(0,0,0,1)

"""

class NumMatrix(object):
    # my way that cannot handle row2, or col2 = 0
    def __init__(self, matrix):
        self.matrix = matrix
        self.block = self.sum_all()

    def sum_all(self):
        if self.matrix == None or self.matrix == [[]]:
            return None
        row = len(self.matrix)
        col = len(self.matrix[0])
        block = [[0 for _ in range(col)] for _ in range(row)]
        total = 0
        for k in range(col):
            total += self.matrix[0][k]
            block[0][k] = total
        total = 0
        for l in range(row):
            total += self.matrix[l][0]
            block[l][0] = total
        for i in range(1,row):
            for j in range(1,col):
                block[i][j] = self.matrix[i][j] + block[i][j-1] + block[i-1][j] - block[i-1][j-1]
        return block

    def sumRegion(self, row1, col1, row2, col2):
        if self.matrix == None or self.matrix == [[]]:
            return None
        if row1 == 0 and col1 == 0:
            return self.block[row2][col2]
        elif row1 == 0:
            return self.block[row2-1][col2-1] - self.block[row2-1][col1-1]
        elif col1 == 0:
            return self.block[row2-1][col2-1] - self.block[row1-1][col2-1]
        return self.block[row2][col2] - self.block[row2][col1-1] - self.block[row1-1][col2] + self.block[row1-1][col1-1]


class NumMatrix2(object):
    def __init__(self, matrix):
        if matrix is None or not matrix:
            return
        n, m = len(matrix), len(matrix[0])
        self.sums = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                self.sums[i][j] = matrix[i - 1][j - 1] + self.sums[i][j - 1] + self.sums[i - 1][j] - self.sums[i - 1][
                    j - 1]

    def sumRegion(self, row1, col1, row2, col2):
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        return self.sums[row2][col2] - self.sums[row2][col1 - 1] - self.sums[row1 - 1][col2] + self.sums[row1 - 1][
            col1 - 1]
"""
