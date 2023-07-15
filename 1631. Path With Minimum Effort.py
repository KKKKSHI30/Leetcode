# Variations of Dijkstra's Algorithm Approach
# Time: O(m⋅nlog(m⋅n))
# Space: O(m⋅n)
# 2023.07.12: yes
from queue import PriorityQueue
class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        row, col = len(heights), len(heights[0])
        min_efforts = [[float('inf') for _ in range(col)] for _ in range(row)]
        min_efforts[0][0] = 0
        pq = PriorityQueue()
        # weight, row, col, val
        pq.put((0, 0, 0, heights[0][0]))
        offsets = [[1,0], [0,1], [-1,0], [0,-1]]
        while not pq.empty():
            cur_weight, cur_row, cur_col, cur_val = pq.get()
            if cur_row == row-1 and cur_col == col-1:
                return cur_weight
            if cur_weight > min_efforts[cur_row][cur_col]:
                continue
            for offset in offsets:
                next_row = cur_row + offset[0]
                next_col = cur_col + offset[1]
                if next_row >= row or next_row < 0 or next_col >= col or next_col < 0:
                    continue
                next_val = heights[next_row][next_col]
                next_weight = max(abs(next_val - cur_val), cur_weight)
                if next_weight < min_efforts[next_row][next_col]:
                    min_efforts[next_row][next_col] = next_weight
                    pq.put((next_weight, next_row, next_col, next_val))

# Union Find - Disjoint Set Approach
# Time: O(m⋅nlog(m⋅n))
# Space: O(m⋅n)
# 2023.07.12: no
class Solution2:
    def minimumEffortPath(self, heights):
        class UnionFind:
            def __init__(self, size):
                self.parent = [x for x in range(size)]
                self.rank = [0]*(size)

            def find(self, i):
                if self.parent[i] != i:
                    self.parent[i] = self.find(self.parent[i])
                return self.parent[i]

            def union(self, x, y):
                parent_x = self.find(x)
                parent_y = self.find(y)
                if parent_x != parent_y:
                    if self.rank[parent_x] > self.rank[parent_y]:
                        self.parent[parent_y] = parent_x
                    elif self.rank[parent_x] < self.rank[parent_y]:
                        self.parent[parent_x] = parent_y
                    else:
                        self.parent[parent_y] = parent_x
                        self.rank[parent_x] += 1

        row = len(heights)
        col = len(heights[0])
        if row == 1 and col == 1:
            return 0

        edge_list = []
        for current_row in range(row):
            for current_col in range(col):
                if current_row > 0:
                    difference = abs(
                        heights[current_row][current_col] -
                        heights[current_row - 1][current_col])
                    edge_list.append(
                        (difference, current_row * col + current_col,
                         (current_row - 1) * col + current_col))
                if current_col > 0:
                    difference = abs(
                        heights[current_row][current_col] -
                        heights[current_row][current_col - 1])
                    edge_list.append(
                        (difference, current_row * col + current_col, current_row
                         * col + current_col - 1))
        edge_list.sort()
        union_find = UnionFind(row*col)

        for difference, x, y in edge_list:
            union_find.union(x, y)
            if union_find.find(0) == union_find.find(row*col-1):
                return difference
        return -1

# Binary Search Using BFS Approach
# Time: O(mn) for sorting
# Space: O(mn)
# 2023.07.12: no
class Solution3:
    def minimumEffortPath(self, heights) -> int:
        row = len(heights)
        col = len(heights[0])
        def canReachDestinaton(mid):
            visited = [[False]*col for _ in range(row)]
            queue = [(0, 0)]  # x, y
            while queue:
                x, y = queue.pop(0)
                if x == row-1 and y == col-1:
                    return True
                visited[x][y] = True
                for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    adjacent_x = x + dx
                    adjacent_y = y + dy
                    if 0 <= adjacent_x < row and 0 <= adjacent_y < col and not visited[adjacent_x][adjacent_y]:
                        current_difference = abs(
                            heights[adjacent_x][adjacent_y]-heights[x][y])
                        if current_difference <= mid:
                            visited[adjacent_x][adjacent_y] = True
                            queue.append((adjacent_x, adjacent_y))
        left = 0
        right = 10000000
        while left < right:
            mid = (left + right)//2
            if canReachDestinaton(mid):
                right = mid
            else:
                left = mid + 1
        return left

# Tests:
test = Solution3()
test.minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]])
test.minimumEffortPath([[1,2,3],[3,8,4],[5,3,5]])
test.minimumEffortPath([[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]])


# Binary Search Using DFS Approach
# Time: O(m⋅nlog(m⋅n)) for sorting
# Space: O(m⋅n)
# 2023.07.12: no
class Solution4:
    def minimumEffortPath(self, heights):
        row = len(heights)
        col = len(heights[0])
        def canReachDestinaton(x, y, mid):
            if x == row-1 and y == col-1:
                return True
            visited[x][y] = True
            for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                adjacent_x = x + dx
                adjacent_y = y + dy
                if 0 <= adjacent_x < row and 0 <= adjacent_y < col and not visited[
                        adjacent_x][adjacent_y]:
                    current_difference = abs(
                        heights[adjacent_x][adjacent_y]-heights[x][y])
                    if current_difference <= mid:
                        visited[adjacent_x][adjacent_y] = True
                        if canReachDestinaton(adjacent_x, adjacent_y, mid):
                            return True
        left = 0
        right = 10000000
        while left < right:
            mid = (left + right)//2
            visited = [[False]*col for _ in range(row)]
            if canReachDestinaton(0, 0, mid):
                right = mid
            else:
                left = mid + 1
        return left

