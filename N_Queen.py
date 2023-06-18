# Ke Shi on Aug 6th, 2022

def N_queens(num):
    """N Queens problem"""
    if (num < 1):
        return 0
    record = [None for _ in range(num)]
    return process(0, record, num)

def process(i, record, num):
    if (i == num):
        return 1
    res =  0
    for j in range(num):
        if (isValid(record, i, j)):
            record[i] = j
            res += process(i+1, record, num)
    return res

def isValid(record, i, j):
    for k in range(i):
        if (j == record[k] or abs(record[k] - j) == abs(i - k)):
            return False
    return True

def N_queens2(num):
    # using bit operation
    if num < 1 or num > 32:
        return 0
    if num == 32:
        limit = -1+(1<<32)   # '0b11111111111111111111111111111111'
    else:
        limit = int(1 << num) -1
    return process2(limit, 0, 0, 0)

def process2(limit, col_limit, left_diag_limit, right_diag_limit):
    if col_limit == limit:
        return 1
    pos = limit & ~(col_limit | left_diag_limit | right_diag_limit)
    res = 0
    while (pos != 0):
        mostrightone = pos & (~pos + 1)
        pos = pos - mostrightone
        res += process2(limit, col_limit | mostrightone, (left_diag_limit | mostrightone) << 1,
                        (right_diag_limit | mostrightone) >> 1)
    return res



results = N_queens(1)
results2 = N_queens(2)
results8 = N_queens(8)

results21 = N_queens2(1)
results22 = N_queens2(2)
results28 = N_queens2(8)