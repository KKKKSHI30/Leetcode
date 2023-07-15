# Union-Find Approach
# Time: O(n)
# Space: O(26)
# 2023.07.05: yes
# notes:重点是先把所有能连的连起来，再考虑别的, 可以用ord不需要hash table
class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        class Union_Find:
            def __init__(self, size):
                self.parent = list(range(size))
                self.rank = [1]*size

            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

            def union(self, x, y):
                xset = self.find(x)
                yset = self.find(y)
                if xset == yset:
                    return
                if self.rank[xset] > self.rank[yset]:
                    self.parent[yset] = xset
                    self.rank[xset] += self.rank[yset]
                else:
                    self.parent[xset] = yset
                    self.rank[yset] += self.rank[xset]
        variables_table = {}
        k = 0
        for j in equations:
            if j[0] not in variables_table:
                variables_table[j[0]] = k
                k += 1
            if j[3] not in variables_table:
                variables_table[j[3]] = k
                k += 1

        ufs = Union_Find(len(variables_table))
        for i in equations:
            if i[1] == "=":
                ufs.union(variables_table[i[0]], variables_table[i[3]])
        for k in equations:
            if k[1] == "!":
                if ufs.find(variables_table[k[0]]) == ufs.find(variables_table[k[3]]):
                    return False
        return True

# Union-Find
# Time: O(n)
# Space: O(n)
# 2023.07.05: yes
# notes: 上面的简短版，效率不高
class Solution2:
    def equationsPossible(self, equations):
        root = list(range(26))

        def find(x):
            if x != root[x]:
                root[x] = find(root[x])
            return root[x]

        def union(x, y):
            x, y = find(x), find(y)
            root[x] = y

        for eqn in equations:
            if eqn[1] == '=':
                x, y = ord(eqn[0])-ord('a'), ord(eqn[3])-ord('a')
                union(x, y)

        for eqn in equations:
            if eqn[1] == '!':
                x, y = ord(eqn[0])-ord('a'), ord(eqn[3])-ord('a')
                if find(x) == find(y):
                    return False
        return True

# DFS Approach
# Time: O(n)
# Space: O(26)
# 2023.07.05: yes
class Solution3:
    def equationsPossible(self, equations):
        graph = [[] for _ in range(26)]

        for eqn in equations:
            if eqn[1] == '=':
                x = ord(eqn[0]) - ord('a')
                y = ord(eqn[3]) - ord('a')
                graph[x].append(y)
                graph[y].append(x)

        color = [-1] * 26

        # mark the color of node as c
        def dfs(node, c):
            if color[node] == -1:
                color[node] = c
                for nei in graph[node]:
                    dfs(nei, c)

        for i in range(26):
            if color[i] == -1:
                dfs(i, i)

        for eqn in equations:
            if eqn[1] == '!':
                x = ord(eqn[0]) - ord('a')
                y = ord(eqn[3]) - ord('a')
                if color[x] == color[y]:
                    return False
        return True

# Tests:
test = Solution3()
test.equationsPossible(["a==b","b!=c","c==a"])
test.equationsPossible(["c==c","b==d","x!=z"])
test.equationsPossible(equations = ["a==b","b!=a"])
test.equationsPossible(equations = ["b==a","a==b"])

