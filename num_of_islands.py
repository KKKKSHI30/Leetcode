# DFS-method
class Solution(object):
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

# Union-Find
from queue import LifoQueue
class union_find_structure(object):
    def __init__(self, value):
        self.value = value

class union_find_sets(object):
    def __init__(self, lstofvalues):
        self.elementMap = {}
        self.fatherMap = {}
        self.sizeMap = {}
        for i in lstofvalues:
            element = union_find_structure(i)
            self.elementMap[i] = element
            self.fatherMap[element] = element
            self.sizeMap[element] = 1

    def find_head(self, element):
        s = LifoQueue()
        element = self.elementMap[element]
        while element != self.fatherMap[element]:
            s.put(element)
            element = self.fatherMap[element]
        # flatten
        while not s.empty():
            self.fatherMap[s.get()] = element
        return element

    def is_same_set(self, element1, element2):
        if element1 in self.elementMap and element2 in self.elementMap:
            return self.find_head(element1).value == self.find_head(element2).value
        return False

    def union(self, element1, element2):
        if element1 in self.elementMap and element2 in self.elementMap:
            ahead = self.find_head(element1)
            bhead = self.find_head(element2)
            if ahead != bhead:
                if self.sizeMap[ahead] > self.sizeMap[bhead]:
                    big = ahead
                    small = bhead
                else:
                    big = bhead
                    small = ahead
                self.fatherMap[small] = big
                self.sizeMap[big] = self.sizeMap[small] + self.sizeMap[big]
                self.sizeMap.pop(small)

test_lst = ["a", "b", "c", "d", "e"]
test = union_find_sets(test_lst)
test.find_head("a")
test.find_head("c")
test.is_same_set("a", "c")
test.union(test_lst[0], test_lst[2])
test.is_same_set("a", "c")
test.union("b", "d")
test.union("b", "e")
test.is_same_set("a", "b")
test.union("a", "b")
test.is_same_set("a", "b")


# num of islands Union-Find method
class Solution2(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0: return 0
        row = len(grid)
        col = len(grid[0])
        self.count = sum(grid[i][j] == '1' for i in range(row) for j in range(col))
        parent = [i for i in range(row * col)]

        def find(x):
            if parent[x] != x:
                return find(parent[x])
            return parent[x]

        def union(x, y):
            xroot, yroot = find(x), find(y)
            if xroot == yroot: return
            parent[xroot] = yroot
            self.count -= 1

        for i in range(row):
            for j in range(col):
                if grid[i][j] == '0':
                    continue
                index = i * col + j
                if j < col - 1 and grid[i][j + 1] == '1':
                    union(index, index + 1)
                if i < row - 1 and grid[i + 1][j] == '1':
                    union(index, index + col)
        return self.count


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
result = Solution2()
result.numIslands(test)
result.numIslands(test2)