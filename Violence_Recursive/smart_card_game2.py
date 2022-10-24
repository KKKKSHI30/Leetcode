def win(lst):
    if lst == None or len(lst) == 0:
        return 0
    else:
        return max(first(lst, 0, len(lst)-1), second(lst, 0, len(lst) -1))

def first(lst, i, j):
    if i == j:
        return lst[i]
    else:
        return max(lst[i] + second(lst, i+1, j), lst[j] + second(lst, i, j-1))

def second(lst, i, j):
    if i == j:
        return 0
    else:
        return min(first(lst, i+1, j), first(lst, i, j-1))

def win2(lst):
    if lst == None or len(lst) == 0:
        return 0
    f = [[0 for _ in range(len(lst))] for _ in range(len(lst))]
    s = [[0 for _ in range(len(lst))] for _ in range(len(lst))]
    for j in range(len(lst)):
        f[j][j] = lst[j]
        for i in range(j-1, -1, -1):
            f[i][j] = max(lst[i] + s[i + 1][j], lst[j] + s[i][j - 1])
            s[i][j] = min(f[i + 1][j], f[i][j - 1])
    return max(f[0][len(lst) - 1], s[0][len(lst) - 1])

test1 = [1, 2, 100, 4]
test2 = [1, 100, 2]
win(test1)  # 101
win(test2)  # 100
win2(test1) # 101
win2(test2) # 100
