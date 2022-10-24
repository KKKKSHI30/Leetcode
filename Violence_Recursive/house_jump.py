def house_jump(x, y, step):
    return process(x, y, step)

def process(x, y, step):
    if (x < 0 or x > 8 or y < 0 or y > 9):
        return 0
    if step == 0:
        return 1 if (x == 0 and y == 0) else 0
    return process(x - 1, y + 2, step - 1)\
           + process(x + 1, y + 2, step - 1)\
           + process(x + 2, y + 1, step - 1)\
           + process(x + 2, y - 1, step - 1)\
           + process(x + 1, y - 2, step - 1)\
           + process(x - 1, y - 2, step - 1)\
           + process(x - 2, y - 1, step - 1)\
           + process(x - 2, y + 1, step - 1)

def house_jump2(x,y, step):
    if (x < 0 or x > 8 or y < 0 or y > 9):
        return 0
    dp = [[[0 for i in range(step + 1)] for j in range(10)] for k in range(9)]
    dp[0][0][0] = 1
    for h in range(1, step+1):
        for r in range(9):
            for c in range(10):
                dp[r][c][h] += getValue(dp, r - 1, c + 2, h - 1)
                dp[r][c][h] += getValue(dp, r + 1, c + 2, h - 1)
                dp[r][c][h] += getValue(dp, r + 2, c + 1, h - 1)
                dp[r][c][h] += getValue(dp, r + 2, c - 1, h - 1)
                dp[r][c][h] += getValue(dp, r + 1, c - 2, h - 1)
                dp[r][c][h] += getValue(dp, r - 1, c - 2, h - 1)
                dp[r][c][h] += getValue(dp, r - 2, c - 1, h - 1)
                dp[r][c][h] += getValue(dp, r - 2, c + 1, h - 1)
    return dp[x][y][step]

def getValue(dp, row, col, height):
    if (row < 0 or row > 8 or col < 0 or col > 9):
        return 0
    return dp[row][col][height]

house_jump(3,3,4) # 36
house_jump(7,7,10) # 515813
house_jump2(3,3,4) # 36
house_jump2(7,7,10) # 515813