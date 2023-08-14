# BFS Approach
# Time: O(mn)
# Space: O(min(m,n))
# 2023.08.03: yes
from collections import deque
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row, col = len(grid), len(grid[0])
        offsets = [[1,0], [0, 1], [-1, 0], [0, -1]]
        count = 0
        def bfs(grid, i, j):
            q = deque()
            cur_count = 0
            q.append([i,j])
            while q:
                cur_row, cur_col = q.popleft()
                if grid[cur_row][cur_col] == 0:
                    continue
                cur_count += 1
                grid[cur_row][cur_col] = 0
                for k in offsets:
                    next_row, next_col = cur_row+k[0], cur_col+k[1]
                    if next_row < 0 or next_row >= row or next_col < 0 or next_col >= col or grid[next_row][next_col] == 0:
                        continue
                    q.append([next_row, next_col])
            return cur_count
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    count = max(count, bfs(grid, i,j))
        return count

# Tests:
test = Solution()
test.maxAreaOfIsland([[1,1,0,0,0],
                      [1,1,0,0,0],
                      [0,0,0,1,1],
                      [0,0,0,1,1]])
test.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],
                      [0,0,0,0,0,0,0,1,1,1,0,0,0],
                      [0,1,1,0,1,0,0,0,0,0,0,0,0],
                      [0,1,0,0,1,1,0,0,1,0,1,0,0],
                      [0,1,0,0,1,1,0,0,1,1,1,0,0],
                      [0,0,0,0,0,0,0,0,0,0,1,0,0],
                      [0,0,0,0,0,0,0,1,1,1,0,0,0],
                      [0,0,0,0,0,0,0,1,1,0,0,0,0]])

# DFS Approach
# Time: O(mn)
# Space: O(mn)
# 2023.08.03: yes
class Solution(object):
    def maxAreaOfIsland(self, grid):
        seen = set()
        def area(r, c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])
                    and (r, c) not in seen and grid[r][c]):
                return 0
            seen.add((r, c))
            return (1 + area(r+1, c) + area(r-1, c) +
                    area(r, c-1) + area(r, c+1))

        return max(area(r, c)
                   for r in range(len(grid))
                   for c in range(len(grid[0])))