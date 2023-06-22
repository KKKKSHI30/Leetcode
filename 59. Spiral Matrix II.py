# Traverse Layer by Layer in Spiral Form
# Time: O(n^2)
# Space: O(1)
# 2023.06.20: yes
# notes: 就是我写的复杂了点，但是思路是一样的
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        visited = [[False for _ in range(n)] for _ in range(n)]
        visited[0][0] = 1
        check1, check2, check3, check4 = True, True, True, True
        i, j, k = 0, 0, 2
        while True:
            while j+1 < n and visited[i][j+1] == 0:
                j += 1
                visited[i][j] = k
                k += 1
                check1 = False
            while i+1 < n and visited[i+1][j] == 0:
                i += 1
                visited[i][j] = k
                k += 1
                check2 = False
            while j-1 >= 0 and visited[i][j-1] == 0:
                j -= 1
                visited[i][j] = k
                k += 1
                check3 = False
            while i-1 >= 0 and visited[i-1][j] == 0:
                i -= 1
                visited[i][j] = k
                k+= 1
                check4 = False
            if check1 and check2 and check3 and check4:
                return visited
            check1, check2, check3, check4 = True, True, True, True

# Optimized spiral traversal
# Time: O(n^2)
# Space: O(1)
# 2023.06.20: no
class Solution2:
    def generateMatrix(self, n):
        result = [[0] * n for _ in range(n)]
        cnt = 1
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        d = 0
        row = 0
        col = 0
        while cnt <= n * n:
            result[row][col] = cnt
            cnt += 1
            r = (row + directions[d][0]) %n
            c = (col + directions[d][1]) % n
            if result[r][c] != 0:
                d = (d + 1) % 4
            row += directions[d][0]
            col += directions[d][1]
        return result


test = Solution2()
test.generateMatrix(3)
