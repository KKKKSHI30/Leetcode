class Solution:
    def generateMatrix(self, n):
        ans = [[0] * n for _ in range(n)]
        DIR = [
            0,
            1,
            0,
            -1,
            0,
        ]  # (r + DIR[i], c + DIR[i+1]) corresponding to move [RIGHT, DOWN, LEFT, TOP]
        r, c = 0, 0  # start at cell (0, 0)
        d = 0  # start with RIGHT direction
        for num in range(1, n * n + 1):
            nr, nc = r + DIR[d], c + DIR[d + 1]
            if (
                not 0 <= nr < n or not 0 <= nc < n or ans[nr][nc] != 0
            ):  # If out of bound or already visited
                d = (d + 1) % 4  # Change next direction
                nr, nc = r + DIR[d], c + DIR[d + 1]

            ans[r][c] = num
            r, c = nr, nc

        return ans


class Solution2(object):
    def generateMatrix(self, n):
        if not n:
            return []
        res = [[0 for _ in range(n)] for _ in range(n)]
        left, right, top, down, num = 0, n - 1, 0, n - 1, 1
        while left <= right and top <= down:
            for i in range(left, right + 1):
                res[top][i] = num
                num += 1
            top += 1
            for i in range(top, down + 1):
                res[i][right] = num
                num += 1
            right -= 1
            for i in range(right, left - 1, -1):
                res[down][i] = num
                num += 1
            down -= 1
            for i in range(down, top - 1, -1):
                res[i][left] = num
                num += 1
            left += 1
        return res
