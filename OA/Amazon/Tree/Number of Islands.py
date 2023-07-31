class Solution(object):
    # dfs
    def numIslands(self, grid):
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    islands += 1
                    self.part_of_island(i,j,grid)
        return islands

    def part_of_island(self, i, j,grid):
        if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] != '1':
            return
        else:
            grid[i][j] = '0'
        self.part_of_island(i,j+1,grid)
        self.part_of_island(i,j-1,grid)
        self.part_of_island(i+1,j,grid)
        self.part_of_island(i-1,j,grid)

from queue import Queue
class Solution2(object):
    # bfs self version 需要优化
    def numIslands(self, grid):
        island = 0
        if grid == None:
            return island
        self.grid_check = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.grid_check[i][j] == False and grid[i][j] == '1':
                    self.smallIsland(grid, i, j)
                    island += 1
        return island

    def smallIsland(self, grid, i, j):
        q = Queue()
        row_length = len(grid)
        column_length = len(grid[0])
        q.put([i,j])
        self.grid_check[i][j] = True
        while not q.empty():
            cur = q.get()
            # cur[0] is row, cur[1] is column
            if cur[1]+1 < column_length:
                if self.grid_check[cur[0]][cur[1] +1] == False:
                    if grid[cur[0]][cur[1] +1] == '1':
                        q.put([cur[0],cur[1] +1])
                    self.grid_check[cur[0]][cur[1] + 1] = True
            if cur[0]+1 < row_length:
                if self.grid_check[cur[0]+1][cur[1]] == False:
                    if grid[cur[0]+1][cur[1]] == '1':
                        q.put([cur[0]+1, cur[1]])
                    self.grid_check[cur[0]+1][cur[1]] = True
            if cur[0]-1 >= 0:
                if self.grid_check[cur[0]-1][cur[1]] == False:
                    if grid[cur[0]-1][cur[1]] == '1':
                        q.put([cur[0]-1, cur[1]])
                    self.grid_check[cur[0] - 1][cur[1]] = True
            if cur[1]-1 >= 0:
                if self.grid_check[cur[0]][cur[1]-1] == False:
                    if grid[cur[0]][cur[1] - 1] == '1':
                        q.put([cur[0], cur[1]-1])
                    self.grid_check[cur[0]][cur[1] - 1] = True

from collections import deque
class Solution3:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        count = 0
        check = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] =='1' and check[i][j]== False:
                    count += 1
                    self.search(grid,check,i,j)
        return count
    def search(self,grid,check,i,j):
        qu = deque([(i,j)])
        while qu:
            i, j = qu.popleft()
            if 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j]=='1' and check[i][j]==False:
                check[i][j] = True
                qu.extend([(i-1,j),(i+1,j),(i,j-1),(i,j+1)])

from queue import Queue
class Solution4(object):
    def numIslands(self, grid):
        island = 0
        if grid == None:
            return island
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.smallIsland(grid, i, j)
                    island += 1
        return island

    def smallIsland(self, grid, i, j):
        q = Queue()
        row_length = len(grid)
        column_length = len(grid[0])
        grid[i][j] = '0'
        q.put([i,j])
        while not q.empty():
            cur = q.get()
            if cur[1]+1 < column_length:
                if grid[cur[0]][cur[1] +1] == '1':
                    q.put([cur[0],cur[1] +1])
                    grid[cur[0]][cur[1]+1] = '0'
            if cur[0]+1 < row_length:
                if grid[cur[0]+1][cur[1]] == '1':
                    q.put([cur[0]+1, cur[1]])
                    grid[cur[0]+1][cur[1]] = '0'
            if cur[0]-1 >= 0:
                if grid[cur[0]-1][cur[1]] == '1':
                    q.put([cur[0]-1, cur[1]])
                    grid[cur[0] - 1][cur[1]] = '0'
            if cur[1]-1 >= 0:
                if grid[cur[0]][cur[1] - 1] == '1':
                    q.put([cur[0], cur[1]-1])
                    grid[cur[0]][cur[1] - 1] = '0'

test = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
test2 = [
  ["1","0","1","1","0"],
  ["0","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
result = Solution3()
result.numIslands(test)
result.numIslands(test2)