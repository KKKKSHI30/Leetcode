# Backtrack
# Time: O((9!)^9)
# Space: O(81)
# 2023.08.03: yes
# notes: 这道题一开始不知道怎么判断是不是在一个小Block里面，
# board[(r // 3) * 3 + i // 3][(c // 3) * 3 + i % 3] == n，用这句非常聪明
# 剩下的倒是backtracking倒是很常规
class Solution:
    def solveSudoku(self, board):
        def backtrack(board, i, j):
            def isValid(board, r, c, n):
                for i in range(9):
                    if board[r][i] == n:
                        return False
                    if board[i][c] == n:
                        return False
                    if board[(r // 3) * 3 + i // 3][(c // 3) * 3 + i % 3] == n:
                        return False
                return True
            m, n = 9, 9
            if j == n:
                # 穷举到最后一列的话就换到下一行重新开始。
                return backtrack(board, i + 1, 0)
            if i == m:
                # 找到一个可行解，触发 base case
                return True

            if board[i][j] != '.':
                # 如果有预设数字，不用我们穷举
                return backtrack(board, i, j + 1)

            for ch in range(ord('1'), ord('9') + 1):
                ch = chr(ch)
                # 如果遇到不合法的数字，就跳过
                if not isValid(board, i, j, ch):
                    continue

                board[i][j] = ch
                # 如果找到一个可行解，立即结束
                if backtrack(board, i, j + 1):
                    return True
                board[i][j] = '.'
                # 穷举完 1~9，依然没有找到可行解，此路不通
            return False
        return backtrack(board, 0, 0)
# Tests:
test = Solution()
test.solveSudoku([["5","3",".",".","7",".",".",".","."],
                  ["6",".",".","1","9","5",".",".","."],
                  [".","9","8",".",".",".",".","6","."],
                  ["8",".",".",".","6",".",".",".","3"],
                  ["4",".",".","8",".","3",".",".","1"],
                  ["7",".",".",".","2",".",".",".","6"],
                  [".","6",".",".",".",".","2","8","."],
                  [".",".",".","4","1","9",".",".","5"],
                  [".",".",".",".","8",".",".","7","9"]])

