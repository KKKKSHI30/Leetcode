class Solution(object):
    def backtracking(self, board, row):
        if row == len(board):
            self.total_results.append(board[:])
            return
        for col in range(len(board)):
            if self.valid(board, row, col):
                board[row] = '.'*(col)+'Q'+'.'*(len(board)-(col+1))
                self.backtracking(board, row+1)
                board[row] = '.'*len(board)

    def valid(self, board, row, col):
        n = len(board)
        for i in range(n):
            if row-i < 0 or col >= n:
                break
            if board[row-i][col] == 'Q':
                return False

        for i in range(n):
            if row-i < 0 or col-i < 0:
                break
            if board[row-i][col-i] == 'Q':
                return False

        for i in range(n):
            if row-i < 0 or col+i >= n:
                break
            if board[row-i][col+i] == 'Q':
                return False
        return True

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board = ['.'*n]*n
        self.total_results = []
        self.backtracking(board, 0)
        return self.total_results

test = Solution()
test.solveNQueens(1)

