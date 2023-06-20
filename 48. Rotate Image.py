# Reverse on Diagonal and then Reverse Left to Right
# Time: O(m)
# Space: O(1)
# 2023.06.19: no
# notes: 很难想到，但是想到了又很好写，旋转90度，最影响想到的就是对角线翻转，这是把行变列的方法
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for row in matrix:
            x, y = 0, len(row)-1
            while x < y:
                row[x], row[y] = row[y], row[x]
                x += 1
                y -= 1

# Rotate Groups of Four Cells
# Time: O(m)
# Space: O(1)
# notes: 这个细节真的很容易错，重点是旋转的话，是4个元素一起旋转，而不是2个了，比较难想
class Solution2:
    def rotate(self, matrix):
        n = len(matrix[0])
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                tmp = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
                matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 -i]
                matrix[j][n - 1 - i] = matrix[i][j]
                matrix[i][j] = tmp

# Tests:
a = [[1,2,3],[4,5,6],[7,8,9]]
test = Solution()
test.rotate(a)

