# BFS Approach
# Time: O(mn)
# Space: O(min(m,n))
# 2023.08.03: yes
from collections import deque
class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row, col = len(grid), len(grid[0])
        offsets = [[1,0], [0, 1], [-1, 0], [0, -1]]
        count = 0
        def bfs(grid, i, j):
            q = deque()
            is_closed = False
            q.append([i,j])
            while q:
                cur_row, cur_col = q.popleft()
                if cur_row == row-1 or cur_col == col-1 or cur_row == 0 or cur_col == 0:
                    is_closed = True
                grid[cur_row][cur_col] = 1
                for k in offsets:
                    next_row, next_col = cur_row+k[0], cur_col+k[1]
                    if next_row < 0 or next_row >= row or next_col < 0 or next_col >= col or grid[next_row][next_col] == 1:
                        continue
                    q.append([next_row, next_col])
            return is_closed
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    if not bfs(grid, i, j):
                        count += 1
        return count

# DFS Approach
# Time: O(mn)
# Space: O(mn)
# 2023.07.13: yes
class Solution2:
    def closedIsland(self, grid):
        m = len(grid)
        n = len(grid[0])
        visit = [[False for _ in range(n)] for _ in range(m)]
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and not visit[i][j] and self.dfs(i, j, m, n, grid, visit):
                    count += 1
        return count

    def dfs(self, x, y, m, n, grid, visit):
        if x < 0 or x >= m or y < 0 or y >= n:
            return False
        if grid[x][y] == 1 or visit[x][y]:
            return True

        visit[x][y] = True
        isClosed = True
        dirx = [0, 1, 0, -1]
        diry = [-1, 0, 1, 0]

        for i in range(4):
            r = x + dirx[i]
            c = y + diry[i]
            if not self.dfs(r, c, m, n, grid, visit):
                isClosed = False

        return isClosed


# Tests:
test = Solution()
test.closedIsland([[0,1,1,1,0],
                   [1,0,1,0,1],
                   [1,0,1,0,1],
                   [1,0,0,0,1],
                   [0,1,1,1,0]])


test.closedIsland([[1,1,1,1,1,1,1,0],
                   [1,0,0,0,0,1,1,0],
                   [1,0,1,0,1,1,1,0],
                   [1,0,0,0,0,1,0,1],
                   [1,1,1,1,1,1,1,0]])

