# Dijkstra's Algorithm Approach
# Time: O(m+ nlogn)
# Space: O(n+m)
# 2023.07.12: yes
from collections import defaultdict, deque
from queue import PriorityQueue
class Solution(object):
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start_node: int
        :type end_node: int
        :rtype: float
        """
        graph = [[] for _ in range(n)]
        for i in range(len(edges)):
            graph[edges[i][0]].append([succProb[i],edges[i][1]])
            graph[edges[i][1]].append([succProb[i],edges[i][0]])

        distTo = [0]*n
        distTo[start_node] = 1
        pq = PriorityQueue()
        pq.put([-1, start_node])
        while not pq.empty():
            cur_prob, cur_node = pq.get()
            cur_prob = -cur_prob
            if cur_node == end_node:
                return cur_prob
            if distTo[cur_node] > cur_prob:
                continue
            for next_node in graph[cur_node]:
                prob_to_next_node = cur_prob*next_node[0]
                if prob_to_next_node > distTo[next_node[1]]:
                    distTo[next_node[1]] = prob_to_next_node
                    pq.put([-prob_to_next_node, next_node[1]])
        return 0

# Bellman-Ford Algorithm Approach
# Time: O(nm)
# Space: O(n)
# 2023.07.12: no
class Solution2:
    def maxProbability(self, n: int, edges, succProb, start, end):
        max_prob = [0] * n
        max_prob[start] = 1

        for i in range(n - 1):
            # If there is no larger probability found during an entire round of updates,
            # stop the update process.
            has_update = 0
            for j in range(len(edges)):
                u, v = edges[j]
                path_prob = succProb[j]
                if max_prob[u] * path_prob > max_prob[v]:
                    max_prob[v] = max_prob[u] * path_prob
                    has_update = 1
                if max_prob[v] * path_prob > max_prob[u]:
                    max_prob[u] = max_prob[v] * path_prob
                    has_update = 1
            if not has_update:
                break

        return max_prob[end]

# Shortest Path Faster Algorithm
# Time: O(nm)
# Space: O(n+m)
# 2023.07.12: no
class Solution3:
    def maxProbability(self, n: int, edges, succProb, start, end):
        graph = defaultdict(list)
        for i, (a, b) in enumerate(edges):
            graph[a].append([b, succProb[i]])
            graph[b].append([a, succProb[i]])

        max_prob = [0.0] * n
        max_prob[start] = 1.0

        queue = deque([start])
        while queue:
            cur_node = queue.popleft()
            for nxt_node, path_prob in graph[cur_node]:

                # Only update max_prob[nxt_node] if the current path increases
                # the probability of reach nxt_node.
                if max_prob[cur_node] * path_prob > max_prob[nxt_node]:
                    max_prob[nxt_node] = max_prob[cur_node] * path_prob
                    queue.append(nxt_node)

        return max_prob[end]


# Tests:
test = Solution3()
test.maxProbability(3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.2], 0, 2)
test.maxProbability(3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.3], 0, 2)
test.maxProbability(3, [[0,1]], [0.5], 0, 2)
