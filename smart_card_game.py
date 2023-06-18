# Ke Shi on Aug 8th, 2022

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

test1 = [1, 2, 100, 4]
test2 = [1, 100, 2]
win(test1)
win(test2)
