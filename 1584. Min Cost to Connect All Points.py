# Minimum Spanning Tree (Using Kruskal's algorithm) Approach
# Time: O(mlogm) for sorting
# Space: O(n)
# 2023.07.06: yes
import heapq
import math

class UnionFind:
    def __init__(self, size: int) -> None:
        self.group = [0] * size
        self.rank = [0] * size

        for i in range(size):
            self.group[i] = i

    def find(self, node: int) -> int:
        if self.group[node] != node:
            self.group[node] = self.find(self.group[node])
        return self.group[node]

    def join(self, node1: int, node2: int) -> bool:
        group1 = self.find(node1)
        group2 = self.find(node2)

        # node1 and node2 already belong to same group.
        if group1 == group2:
            return False

        if self.rank[group1] > self.rank[group2]:
            self.group[group2] = group1
        elif self.rank[group1] < self.rank[group2]:
            self.group[group1] = group2
        else:
            self.group[group1] = group2
            self.rank[group2] += 1

        return True


class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)
        all_edges = []

        for curr_node in range(n):
            for next_node in range(curr_node + 1, n):
                weight = abs(points[curr_node][0] - points[next_node][0]) + \
                         abs(points[curr_node][1] - points[next_node][1])
                all_edges.append((weight, curr_node, next_node))

        # Sort all edges in increasing order.
        all_edges.sort()

        uf = UnionFind(n)
        mst_cost = 0
        edges_used = 0

        for weight, node1, node2 in all_edges:
            if uf.join(node1, node2):
                mst_cost += weight
                edges_used += 1
                if edges_used == n - 1:
                    break
        return mst_cost


# Prim Approach
# Time: O(n^2 logn)
# Space: O(n^2)
# 2023.07.06: no
# notes: 造一个fake head,初始heap = [(0,0)], 后面的0代表的是一个节点，第0个节点，对应到points即可
class Solution2:
    def minCostConnectPoints(self, points):
        n = len(points)

        # Min-heap to store minimum weight edge at top.
        heap = [(0, 0)]

        # Track nodes which are included in MST.
        in_mst = [False] * n

        mst_cost = 0
        edges_used = 0

        while edges_used < n:
            weight, curr_node = heapq.heappop(heap)

            # If node was already included in MST we will discard this edge.
            if in_mst[curr_node]:
                continue

            in_mst[curr_node] = True
            mst_cost += weight
            edges_used += 1

            for next_node in range(n):
                # If next node is not in MST, then edge from curr node
                # to next node can be pushed in the priority queue.
                if not in_mst[next_node]:
                    next_weight = abs(points[curr_node][0] - points[next_node][0]) + \
                                  abs(points[curr_node][1] - points[next_node][1])

                    heapq.heappush(heap, (next_weight, next_node))

        return mst_cost


# Prim Optimized Approach
# Time: O(n^2) for sorting
# Space: O(n)
# 2023.07.06: no
# 相比于上一步，用一个数组进行记录最短的是多少，就不用每次比较这么多了
class Solution3:
    def minCostConnectPoints(self, points):
        n = len(points)
        mst_cost = 0
        edges_used = 0

        # Track nodes which are visited.
        in_mst = [False] * n

        min_dist = [math.inf] * n
        min_dist[0] = 0

        while edges_used < n:
            curr_min_edge = math.inf
            curr_node = -1

            # Pick least weight node which is not in MST.
            for node in range(n):
                if not in_mst[node] and curr_min_edge > min_dist[node]:
                    curr_min_edge = min_dist[node]
                    curr_node = node

            mst_cost += curr_min_edge
            edges_used += 1
            in_mst[curr_node] = True

            # Update adjacent nodes of current node.
            for next_node in range(n):
                weight = abs(points[curr_node][0] - points[next_node][0]) + \
                         abs(points[curr_node][1] - points[next_node][1])

                if not in_mst[next_node] and min_dist[next_node] > weight:
                    min_dist[next_node] = weight

        return mst_cost

# Tests:
test = Solution3()
test.minCostConnectPoints(points = [[0,0],[2,2],[3,10],[5,2],[7,0]])


