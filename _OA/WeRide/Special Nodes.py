from collections import deque, defaultdict
import sys
# This is important !!!!!!!!!!!!!!!!
sys.setrecursionlimit(10**5)
def dfs(x, p, con, d, maxd, nodes):
    if d > maxd[0]:
        maxd[0] = d
        nodes.clear()
    if d == maxd[0]:
        nodes.append(x)
    for y in con[x]:
        if y != p:
            dfs(y, x, con, d + 1, maxd, nodes)
def isSpecial(n, tree_from, tree_to):
    e = [[] for _ in range(n)]
    for i in range(len(tree_from)):
        e[tree_from[i] - 1].append(tree_to[i] - 1)
        e[tree_to[i] - 1].append(tree_from[i] - 1)
    con = [set() for _ in range(n)]
    for i in range(n):
        con[i] = set(e[i])
    nodes = set(range(n))
    q = []
    for i in range(n):
        if len(con[i]) == 1:
            q.append(i)
    while q and len(nodes) > 2:
        for _ in range(len(q)):
            x = q.pop(0)
            y = next(iter(con[x]))
            nodes.remove(x)
            con[y].remove(x)
            if len(con[y]) == 1:
                q.append(y)
    ind1 = []
    ind2 = []
    m = [0]
    if len(nodes) == 1:
        dfs(next(iter(nodes)), -1, e, 0, m, ind1)
    else:
        t1, t2 = list(nodes)
        dfs(t1, t2, e, 0, m, ind1)
        dfs(t2, t1, e, 0, m, ind2)
    r = [0] * n
    for i in ind1:
        r[i] = 1
    for i in ind2:
        r[i] = 1
    return r
def print_result(v):
    print(" ".join(map(str, v)))
tree_from = [1, 2, 3]
tree_to = [2, 3, 4]
print_result(isSpecial(4, tree_from, tree_to))