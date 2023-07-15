# Breadth-First Search Approach
# Time: O(mn)
# Space: O(mn)
# 2023.07.14: yes
from collections import deque
class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        row, col = len(heights), len(heights[0])
        pacific_queue = deque()
        atlantic_queue = deque()
        for i in range(row):
            pacific_queue.append((i, 0))
            atlantic_queue.append((i, col - 1))
        for i in range(col):
            pacific_queue.append((0, i))
            atlantic_queue.append((row - 1, i))
        offsets = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        def bfs(q):
            reachable = set()
            while q:
                cur_row, cur_col = q.popleft()
                reachable.add((cur_row, cur_col))
                for offset in offsets:
                    new_row, new_col = cur_row + offset[0], cur_col + offset[1]
                    if new_row < 0 or new_row >= row or new_col < 0 or new_col >= col:
                        continue
                    if (new_row, new_col) in reachable:
                        continue
                    if heights[new_row][new_col] < heights[cur_row][cur_col]:
                        continue
                    q.append((new_row, new_col))
            return reachable
        pr = bfs(pacific_queue)
        ar = bfs(atlantic_queue)
        return list(pr.intersection(ar))


# Depth First Search Approach
# Time: O(mn)
# Space: O(mn)
# 2023.07.14: yes
class Solution2:
    def pacificAtlantic(self, matrix):
        if not matrix or not matrix[0]:
            return []
        num_rows, num_cols = len(matrix), len(matrix[0])
        pacific_reachable = set()
        atlantic_reachable = set()
        def dfs(row, col, reachable):
            reachable.add((row, col))
            for (x, y) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                new_row, new_col = row + x, col + y
                if new_row < 0 or new_row >= num_rows or new_col < 0 or new_col >= num_cols:
                    continue
                if (new_row, new_col) in reachable:
                    continue
                if matrix[new_row][new_col] < matrix[row][col]:
                    continue
                dfs(new_row, new_col, reachable)

        for i in range(num_rows):
            dfs(i, 0, pacific_reachable)
            dfs(i, num_cols - 1, atlantic_reachable)
        for i in range(num_cols):
            dfs(0, i, pacific_reachable)
            dfs(num_rows - 1, i, atlantic_reachable)
        return list(pacific_reachable.intersection(atlantic_reachable))







# Tests:
test = Solution()
test.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])

