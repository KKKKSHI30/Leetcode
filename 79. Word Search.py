# Backtracking
# Time: O(n3^l)
# Space: O(l)
# 2023.07.14: yes
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def backtracking(cur_row, cur_col, word):
            if len(word) == 0:
                return True
            if board[cur_row][cur_col] == word[0]:
                tmp = board[cur_row][cur_col]
                board[cur_row][cur_col] = "#"
                offsets = [[0,1], [1,0], [-1,0], [0,-1]]
                for offset in offsets:
                    new_row, new_col = cur_row+offset[0], cur_col+offset[1]
                    if new_row < 0 or row <= new_row or new_col < 0 or col <= new_col:
                        continue
                    ret = backtracking(new_row, new_col, word[1:])
                    if ret:
                        return True
                board[cur_row][cur_col] = tmp

        row, col = len(board), len(board[0])
        if row == 1 and col == 1:
            return board[0][0] == word
        for i in range(row):
            for j in range(col):
                if backtracking(i, j, word):
                    return True
        return False

# Tests:
test = Solution()
test.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB")
test.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"SEE")
test.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED")
