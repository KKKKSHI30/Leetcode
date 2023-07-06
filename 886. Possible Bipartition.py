# Depth-First Search Approach
# Time: O(n)
# Space: O(n)
# 2023.07.05: yes
from collections import deque

class Solution(object):
    def possibleBipartition(self, n, dislikes):
        """
        :type n: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        def traverse(graph, node):
            if self.biparted == False:
                return
            self.visited[node] = True
            for next_node in graph[node]:
                if not self.visited[next_node]:
                    self.color[next_node] = not self.color[node]
                    traverse(graph, next_node)
                else:
                    if self.color[next_node] == self.color[node]:
                        self.biparted = False
                        return
        if n == 0 or n == 1:
            return True
        self.color = [False]*(n+1)
        self.visited = [False]*(n+1)
        self.biparted = True
        graph = [[] for _ in range(n+1)]
        for i in dislikes:
            graph[i[0]].append(i[1])
        for j in range(1, len(graph)):
            traverse(graph, j)
        return self.biparted

# Breadth-First Search Approach
# Time: O(n)
# Space: O(n)
# 2023.07.05: yes
class Solution2:
    def possibleBipartition(self, n, dislikes):
        def bfs(source):
            q = deque([source])
            color[source] = 0  # Start with marking source as 'RED'
            while q:
                node = q.popleft()
                for neighbor in adj[node]:
                    # If there is a conflict, return false.
                    if color[neighbor] == color[node]: return False
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - color[node]
                        q.append(neighbor)
            return True

        adj = [[] for _ in range(n + 1)]
        for dislike in dislikes:
            adj[dislike[0]].append(dislike[1])
            adj[dislike[1]].append(dislike[0])

        color = [-1] * (n + 1)  # 0 stands for red and 1 stands for blue.
        for i in range(1, n + 1):
            if color[i] == -1:
                # For each pending component, run BFS.
                if not bfs(i):
                    # Return false, if there is conflict in the component.
                    return False
        return True

# Union-Find Approach
# Time: O(n+e)
# Space: O(n+e)
# 2023.07.05: yes
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union_set(self, x, y):
        xset = self.find(x)
        yset = self.find(y)
        if xset == yset:
            return

        if self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset
        elif self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset
        else:
            self.parent[yset] = xset
            self.rank[xset] += 1

class Solution3:
    def possibleBipartition(self, n, dislikes):
        adj = [[] for _ in range(n + 1)]
        for dislike in dislikes:
            adj[dislike[0]].append(dislike[1])
            adj[dislike[1]].append(dislike[0])

        dsu = UnionFind(n + 1)
        for node in range(1, n + 1):
            for neighbor in adj[node]:
                # Check if the node and its neighbor is in the same set.
                if dsu.find(node) == dsu.find(neighbor): return False
                # Move all the neighbours into same set as the first neighbour.
                dsu.union_set(adj[node][0], neighbor)
        return True

# Tests:
test = Solution3()
test.possibleBipartition(n = 3, dislikes = [[1,2],[1,3],[2,3]])
test.possibleBipartition(n = 4, dislikes = [[1,2],[1,3],[2,4]])