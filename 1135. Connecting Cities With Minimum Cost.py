# Minimum Spanning Tree (Using Kruskal's algorithm) Approach
# Time: O(mlogm) for sorting
# Space: O(n)
# 2023.07.06: yes


class UnionFind:
    def __init__(self, n):
        self.parent = [node for node in range(n)]
        self.size = [1] * n
        self.count = n-1

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def connected(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        return rootP == rootQ

    def union(self, A, B):
        root_A = self.find(A)
        root_B = self.find(B)
        if root_A == root_B:
            return
        if self.size[root_A] < self.size[root_B]:
            self.parent[root_A] = root_B
            self.size[root_B] += self.size[root_A]
        else:
            self.parent[root_B] = root_A
            self.size[root_A] += self.size[root_B]
        self.count -= 1

class Solution(object):
    def minimumCost(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        mst = 0
        ufs = UnionFind(n+1)
        sorted_connections = sorted(connections, key=lambda x: x[2])
        for connection in sorted_connections:
            if ufs.connected(connection[0], connection[1]):
                continue
            else:
                ufs.union(connection[0], connection[1])
                mst += connection[2]
        return mst if ufs.count==1 else -1

# Prim Approach
# Time: O(eloge)
# Space: O(e+v)
# 2023.07.06: yes
# notes: 看prim的笔记

import heapq
class Prim:
    # 核心数据结构，存储「横切边」的优先级队列
    def __init__(self, graph):
        self.graph = graph
        self.pq = []  # PriorityQueue<int[]> 的实现
        self.inMST = [False] * len(graph)  # 类似 visited 数组的作用，记录哪些节点已经成为最小生成树的一部分
        self.weightSum = 0  # 记录最小生成树的权重和
        self.inMST[0]= True  # 随便从一个点开始切分都可以，我们不妨从节点 0 开始
        self.cut(0)
        # 不断进行切分，向最小生成树中添加边
        while self.pq:
            # 按照边的权重从小到大排序
            edge = heapq.heappop(self.pq)
            to = edge[2]  # 表示相邻节点
            weight = edge[0]  # 表示这条边的权重
            if self.inMST[to]:  # 节点 to 已经在最小生成树中，跳过。否则这条边会产生环
                continue
            self.weightSum += weight  # 将边 edge 加入最小生成树
            self.inMST[to] = True
            self.cut(to)  # 节点 to 加入后，进行新一轮切分，会产生更多横切边

    # 将 s 的横切边加入优先队列
    def cut(self, s):
        for edge in self.graph[s]:  # 遍历 s 的邻边
            to = edge[2]  # 相邻的节点
            if self.inMST[to]:  # 相邻接点 to 已经在最小生成树中，跳过
                continue
            heapq.heappush(self.pq, edge)  # 加入横切边队列

    # 最小生成树的权重和
    def weight(self):
        return self.weightSum

    # 判断最小生成树是否包含图中的所有节点
    def allConnected(self) -> bool:
        for i in range(len(self.inMST)):
            if not self.inMST[i]:
                return False
        return True

class Solution2(object):
    def minimumCost(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        graph = [[] for _ in range(n)]
        for connection in connections:
            u = connection[0]-1
            v = connection[1]-1
            graph[u].append([connection[2],u,v])
            graph[v].append([connection[2],v,u])
        prim = Prim(graph)
        if not prim.allConnected():
            return -1
        return prim.weight()
# Test:
test = Solution2()
test.minimumCost(n=3, connections=[[1, 2, 5], [1, 3, 6], [2, 3, 1]])
test.minimumCost(n = 4, connections = [[1,2,3],[3,4,4]])