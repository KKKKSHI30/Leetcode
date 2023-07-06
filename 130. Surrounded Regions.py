# Depth-First Search Approach
# Time: O(n)
# Space: O(n)
# 2023.07.05: no
from itertools import product
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        self.ROWS = len(board)
        self.COLS = len(board[0])
        # Step 1). retrieve all border cells
        borders = list(product(range(self.ROWS), [0, self.COLS-1])) \
                + list(product([0, self.ROWS-1], range(self.COLS)))
        # Step 2). mark the "escaped" cells, with any placeholder, e.g. 'E'
        for row, col in borders:
            self.DFS(board, row, col)
        # Step 3). flip the captured cells ('O'->'X') and the escaped one ('E'->'O')
        for r in range(self.ROWS):
            for c in range(self.COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'  # captured
                elif board[r][c] == 'E':
                    board[r][c] = 'O'  # escaped

    def DFS(self, board, row, col):
        if board[row][col] != 'O':
            return
        board[row][col] = 'E'
        if col < self.COLS-1:
            self.DFS(board, row, col+1)
        if row < self.ROWS-1:
            self.DFS(board, row+1, col)
        if col > 0:
            self.DFS(board, row, col-1)
        if row > 0:
            self.DFS(board, row-1, col)

# Breadth-First Search Approach
# Time: O(n)
# Space: O(n)
# 2023.07.05: no
class Solution2(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        self.ROWS = len(board)
        self.COLS = len(board[0])

        # Step 1). retrieve all border cells
        from itertools import product
        borders = list(product(range(self.ROWS), [0, self.COLS-1])) \
                + list(product([0, self.ROWS-1], range(self.COLS)))

        # Step 2). mark the "escaped" cells, with any placeholder, e.g. 'E'
        for row, col in borders:
            #self.DFS(board, row, col)
            self.BFS(board, row, col)

        # Step 3). flip the captured cells ('O'->'X') and the escaped one ('E'->'O')
        for r in range(self.ROWS):
            for c in range(self.COLS):
                if board[r][c] == 'O':   board[r][c] = 'X'  # captured
                elif board[r][c] == 'E': board[r][c] = 'O'  # escaped


    def BFS(self, board, row, col):
        from collections import deque
        queue = deque([(row, col)])
        while queue:
            (row, col) = queue.popleft()
            if board[row][col] != 'O':
                continue
            # mark this cell as escaped
            board[row][col] = 'E'
            # check its neighbor cells
            if col < self.COLS-1:
                queue.append((row, col+1))
            if row < self.ROWS-1:
                queue.append((row+1, col))
            if col > 0:
                queue.append((row, col-1))
            if row > 0:
                queue.append((row-1, col))


# Union-Find Approach
# Time: O(v+e)
# Space: O(v+e)
# 2023.07.05: no
# notes: DFS和BFS更好，但是这只是个思路
class Union_Find:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xset = self.find(x)
        yset = self.find(y)
        if xset == yset:
            return
        if self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset
        elif self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset
        else:
            self.parent[yset] = xset
            self.rank[xset] += 1

    def connected(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        return rootP == rootQ

class Solution3(object):
    def solve(self, board) -> None:
        if not board:
            return
        m = len(board)
        n = len(board[0])
        # 给 dummy 留一个额外位置
        uf = Union_Find(m * n + 1)
        dummy = m * n
        # 将首列和末列的 O 与 dummy 连通
        for i in range(m):
            if board[i][0] == 'O':
                uf.union(i * n, dummy)
            if board[i][n - 1] == 'O':
                uf.union(i * n + n - 1, dummy)
        # 将首行和末行的 O 与 dummy 连通
        for j in range(n):
            if board[0][j] == 'O':
                uf.union(j, dummy)
            if board[m - 1][j] == 'O':
                uf.union(n * (m - 1) + j, dummy)
        # 方向数组 d 是上下左右搜索的常用手法
        d = [[1, 0], [0, 1], [0, -1], [-1, 0]]
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if board[i][j] == 'O':
                    # 将此 O 与上下左右的 O 连通
                    for k in range(4):
                        x = i + d[k][0]
                        y = j + d[k][1]
                        if board[x][y] == 'O':
                            uf.union(x * n + y, i * n + j)
        # 所有不和 dummy 连通的 O，都要被替换
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if not uf.connected(dummy, i * n + j):
                    board[i][j] = 'X'

# Tests:
test = Solution()
test.solve(board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])
