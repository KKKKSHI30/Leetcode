# Dynamic Programming 1D recursion
# Time: O(mn)
# Space: O(m)
# 2023.07.26: no
# notes: 直接用1D table，真的强， 价格是j， K是i的值，然后把k优化掉，用一个一行来记录上一层k的值
class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        price_table = [float('inf') for _ in range(n)]
        # price of source must be 0
        price_table[src] = 0
        # initialization with 0 transfer
        for source, destination, ticket_price in flights:
            if source == src:
                price_table[destination] = ticket_price
        # tranfer k times to update price table
        for trasfer in range(0, K):
            current_price = [*price_table]
            for source, destination, ticket_price in flights:
                current_price[destination] = min(current_price[destination], price_table[source] + ticket_price)
            # update current price back to price table
            price_table = current_price
        if price_table[dst] == float('inf'):
            return -1
        else:
            return price_table[dst]


# Breadth First Search
# Time: O(n+ek)
# Space: O(n+ek)
# 2023.07.26: no
# notes: 非常像Dijkstra，符合条件的push的queue里面，根据k的次数来遍历，每次把所有符合的都Push进去
from collections import defaultdict, deque

class Solution2:
    def findCheapestPrice(self, n, flights, src, dst, k):
        adj = defaultdict(list)
        for i in flights:
            adj[i[0]].append((i[1], i[2]))
        dist = [float('inf')] * n
        q = deque()
        q.append((src, 0))
        stops = 0
        while stops <= k and q:
            sz = len(q)
            # Iterate on the current level.
            for _ in range(sz):
                node, distance = q.popleft()
                if node not in adj:
                    continue
                # Loop over neighbors of the popped node.
                for neighbor, price in adj[node]:
                    if price + distance >= dist[neighbor]:
                        continue
                    dist[neighbor] = price + distance
                    q.append((neighbor, dist[neighbor]))
            stops += 1
        return -1 if dist[dst] == float('inf') else dist[dst]

# Bellman Ford
# Time: O((n+e)k)
# Space: O(n)
# 2023.07.26: no
# notes: 1D DP的简单版，没有Base的情况
class Solution3:
    def findCheapestPrice(self, n, flights, src, dst, k):
        # Distance from source to all other nodes.
        dist = [float('inf')] * n
        dist[src] = 0

        # Run only K+1 times since we want the shortest distance in K hops
        for i in range(k + 1):
            # Create a copy of the dist list.
            temp = dist[:]
            for flight in flights:
                if dist[flight[0]] != float('inf'):
                    temp[flight[1]] = min(temp[flight[1]], dist[flight[0]] + flight[2])
            # Copy the temp list into dist.
            dist = temp

        return -1 if dist[dst] == float('inf') else dist[dst]


# Dijkstra
# Time: O((n+e)k)
# Space: O(n)
# 2023.07.26: no
# notes: 和bfs不同的是，需要记录k的次数，以权重为pop出来的条件
import heapq
class Solution4:
    def findCheapestPrice(self, n, flights, src, dst, k):
        adj = {}
        for i in flights:
            adj.setdefault(i[0], []).append((i[1], i[2]))
        stops = [float('inf')] * n
        pq = [(0, src, 0)]  # (dist_from_src_node, node, number_of_stops_from_src_node)
        while pq:
            dist, node, steps = heapq.heappop(pq)
            # We have already encountered a path with a lower cost and fewer stops,
            # or the number of stops exceeds the limit.
            if steps > stops[node] or steps > k + 1:
                continue
            stops[node] = steps
            if node == dst:
                return dist
            if node in adj:
                for a in adj[node]:
                    heapq.heappush(pq, (dist + a[1], a[0], steps + 1))
        return -1


# Tests:
test = Solution4()
test.findCheapestPrice(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1)

