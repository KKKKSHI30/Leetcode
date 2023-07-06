# Depth-First Search Approach
# Time: O(n+e)
# Space: O(n+e)
# 2023.07.05: yes
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        def traverse(node):
            if self.visited[node] == True:
                return
            self.visited[node] = True
            for next_node in self.graph[node]:
                if self.visited[next_node] == False:
                    traverse(next_node)

        self.graph = [[] for _ in range(n)]
        self.visited = [False] * n
        components = 0
        for i in edges:
            self.graph[i[0]].append(i[1])
            self.graph[i[1]].append(i[0])
        for j in range(n):
            if self.visited[j] == False:
                traverse(j)
                components += 1
        return components

# Union-Find Approach
# Time: O(e)
# Space: O(v)
# 2023.07.05: yes
class Solution2(object):
    def countComponents(self, n, edges):
        class Union_Find:
            def __init__(self, n):
                self.count = n
                self.parent = [i for i in range(n)]
                self.size = [1] * n

            def union(self, p, q):
                rootP = self.find(p)
                rootQ = self.find(q)
                if rootP == rootQ:
                    return
                if self.size[rootP] > self.size[rootQ]:
                    self.parent[rootQ] = rootP
                    self.size[rootP] += self.size[rootQ]
                else:
                    self.parent[rootP] = rootQ
                    self.size[rootQ] += self.size[rootP]
                self.count -= 1

            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]
        ufs = Union_Find(n)
        for e in edges:
            ufs.union(e[0], e[1])
        return ufs.count

test = Solution2()
test.countComponents(n = 5, edges = [[0,1],[1,2],[3,4]])
test.countComponents(n = 5, edges = [[0,1],[1,2],[2,3],[3,4]])