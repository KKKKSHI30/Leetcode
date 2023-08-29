class Solution(object):
    def rotate(self, matrix):
        row, col = len(matrix), len(matrix[0])
        new_matrix = [[0 for _ in range(row)] for _ in range(col)]
        for i in range(col):
            for j in range(row):
                new_matrix[i][j] = matrix[j][i]
        for row in new_matrix:
            x, y = 0, len(row)-1
            while x < y:
                row[x], row[y] = row[y], row[x]
                x += 1
                y -= 1
        print(new_matrix)



# 1 2 3
# 4 5 6
# 7 8 9
# 10 11 12

# 1 4 7 10
# 2 5 8 11
# 3 6 9 12

# 10 7 4 1
# 11 8 5 2
# 12 9 6 3
a = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
test = Solution()
b = test.rotate(a)
b = [[10, 7, 4, 1], [11, 8, 5, 2], [12, 9, 6, 3]]

for i in range(3):
    for j in range(4):
        print(b[i][j], end = " ")
    print()

