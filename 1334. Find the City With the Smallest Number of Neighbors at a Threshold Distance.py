# Array Approach
# Time: O(n^3)
# Space: O(n)
# 2023.07.22: yes
# notes: 根据k的不同，通过dp不断updateedges，方法不太好，不推荐
import collections
import heapq

class Solution(object):
    def findTheCity(self, n, edges, maxd):
        dis = [[float('inf')] * n for _ in range(n)]
        for i, j, w in edges:
            dis[i][j] = dis[j][i] = w
        for i in range(n):
            dis[i][i] = 0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
        res = {sum(d <= maxd for d in dis[i]): i for i in range(n)}
        return res[min(res)]

# Dijkstra
# Time: O(n^2)
# Space: O(n)
# 2023.07.22: yes
# notes: 从每一个点开始，求dijkstra，算出每一个到任何一个点的最短距离，如果超过threshold，就不压栈了
# 然后求出最少的数量，和最大的数字
class Solution2:
    def findTheCity(self, n, edges, distanceThreshold):
        graph = collections.defaultdict(list)

        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        def getNumberOfNeighbors(city):
            heap = [(0, city)]
            dist = {}

            while heap:
                currW, u = heapq.heappop(heap)
                if u in dist:
                    continue
                if u != city:
                    dist[u] = currW
                for v, w in graph[u]:
                    if v in dist:
                        continue
                    if currW + w <= distanceThreshold:
                        heapq.heappush(heap, (currW + w, v))
            return len(dist)

        return max([(getNumberOfNeighbors(city), city) for city in range(n)], key=lambda x: (-x[0], x[1]))[-1]

# Tests:
test = Solution2()
test.findTheCity(4, [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], 4)