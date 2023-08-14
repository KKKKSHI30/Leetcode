import heapq
from collections import deque


class Solution(object):
    def maximumSafenessFactor(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def manhanttan(x, y):
            min_dis = float("inf")
            for a, b in thiefs:
                min_dis = min(min_dis, abs(a-x) + abs(b-y))
            return min_dis
        n = len(grid)
        offsets = [[1,0], [0,1], [-1,0], [0, -1]]
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return 0
        thiefs = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    thiefs.append([i, j])
        visited = [[False for _ in range(n)] for _ in range(n)]
        min_weight = -(manhanttan(0,0))
        q = [(min_weight, 0, 0)]
        visited[0][0] = True
        while q:
            weight, cur_x, cur_y = heapq.heappop(q)
            min_weight = max(min_weight, weight)
            if cur_x == n-1 and cur_y == n-1:
                return -min_weight
            for i in offsets:
                new_x, new_y = cur_x + i[0], cur_y + i[1]
                if new_x < 0 or new_x >= n or new_y < 0 or new_y >= n:
                    continue
                else:
                    if visited[new_x][new_y]:
                        continue
                    visited[new_x][new_y] = True
                    heapq.heappush(q, (-manhanttan(new_x, new_y), new_x, new_y))

# notes: 和我的唯一区别就是，先把所以得距离算出来，根据thief向外延，就不用重复运算Manhatton了，emo了
class Solution2:
    def maximumSafenessFactor(self, grid):
        n = len(grid)
        q = deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    q.append((i, j))

        while q:
            for _ in range(len(q)):
                x, y = q.popleft()

                for i, j in [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]:
                    if 0 <= i < n and 0 <= j < n and grid[i][j] == 0:
                        q.append((i, j))
                        grid[i][j] = grid[x][y] + 1

        q = [(-grid[0][0], 0, 0)]
        seen = set([(0, 0)])
        res = float("inf")

        while q:
            for i in range(len(q)):
                w, x, y = heapq.heappop(q)
                res = min(res, -w)

                if x == y == n - 1:
                    return res - 1

                for i, j in [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]:
                    if 0 <= i < n and 0 <= j < n and (i, j) not in seen:
                        heapq.heappush(q, (-grid[i][j], i, j))
                        seen.add((i, j))

# notes: 代码是丑陋了点，但是思路还是不错的lol
class Solution3:
    def maximumSafenessFactor(self, grid):
        n = len(grid)
        queue = deque()
        new_grid = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        visited = set()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append([i, j, 0])
                    visited.add((i, j))
        ans = 0
        # if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        #     return 0

        while len(queue) > 0:
            i, j, dist = queue.popleft()
            new_grid[i][j] = dist

            if i + 1 < n and (i + 1, j) not in visited and grid[i + 1][j] == 0:
                visited.add((i + 1, j))
                queue.append([i + 1, j, dist + 1])

            if i - 1 >= 0 and (i - 1, j) not in visited and grid[i - 1][j] == 0:
                visited.add((i - 1, j))
                queue.append([i - 1, j, dist + 1])

            if j - 1 >= 0 and (i, j - 1) not in visited and grid[i][j - 1] == 0:
                visited.add((i, j - 1))
                queue.append([i, j - 1, dist + 1])

            if j + 1 < n and (i, j + 1) not in visited and grid[i][j + 1] == 0:
                visited.add((i, j + 1))
                queue.append([i, j + 1, dist + 1])

        def good(val):
            queue = deque()
            queue.append([0, 0])
            visited = set()
            visited.add((0, 0))
            if new_grid[0][0] < val:
                return False
            while len(queue) > 0:
                i, j = queue.popleft()
                if (i, j) == (n - 1, n - 1):
                    return True
                if i + 1 < n and new_grid[i + 1][j] >= val and (i + 1, j) not in visited:
                    queue.append([i + 1, j])
                    visited.add((i + 1, j))
                if i - 1 >= 0 and new_grid[i - 1][j] >= val and (i - 1, j) not in visited:
                    queue.append([i - 1, j])
                    visited.add((i - 1, j))

                if j + 1 < n and new_grid[i][j + 1] >= val and (i, j + 1) not in visited:
                    queue.append([i, j + 1])
                    visited.add((i, j + 1))

                if j - 1 >= 0 and new_grid[i][j - 1] >= val and (i, j - 1) not in visited:
                    queue.append([i, j - 1])
                    visited.add((i, j - 1))

            return False

        l, h, ans = 0, 10 ** 3, -1
        while l <= h:
            mid = (l + h) // 2
            if good(mid):
                ans = mid
                l = mid + 1
            else:
                h = mid - 1

        return ans

# Tests:
test = Solution3()
test.maximumSafenessFactor([[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]])
test.maximumSafenessFactor([[1,0,0],[0,0,0],[0,0,1]])
test.maximumSafenessFactor([[0,0,1],
                            [0,0,0],
                            [0,0,0]])






