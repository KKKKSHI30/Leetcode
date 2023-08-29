# Brute Force
# Time: O(n^3)
# Space: O(n)
# 2023.08.18: yes
# notes: 根据n^3直接随机选择3个点，看他们是不是互相的分支，是的话，-6就是最终答案，因为中间的6条边不算
# 没有标答，https://leetcode.com/problems/minimum-degree-of-a-connected-trio-in-a-graph/solutions/1204311/python-sorting-degree-with-explanation-details/
# 上面是参考答案
from collections import defaultdict
from itertools import combinations

class Solution(object):
    def minTrioDegree(self, n, edges):
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        min_degree = float('inf')
        for u in range(1, n + 1):
            for v, w in combinations(graph[u], 2):
                if v in graph[w]:
                    min_degree = min(min_degree, len(graph[u]) + len(graph[v]) + len(graph[w]) - 6)
        return min_degree if min_degree != float('inf') else -1

# Brute Force
# Time: O(n^3)
# Space: O(n)
# 2023.08.18: yes
# notes: 只是基于一些上面的优化，比如sort根据大的排序，如果当前边小于3了，说明不可能有别的，直接返回
class Solution2(object):
    def minTrioDegree(self, n, edges):
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        min_degree = float('inf')
        for u in sorted(range(1, n + 1), key=lambda x: len(graph[x])):
            if len(graph[u]) >= min_degree / 3:
                break
            for v in graph[u]:
                for w in graph[v]:
                    if w in graph[u]:
                        min_degree = min(min_degree, len(graph[u]) + len(graph[v]) + len(graph[w]))
        return min_degree - 6 if min_degree != float('inf') else -1

# Tests:
test = Solution()
test.minTrioDegree(n = 6, edges = [[1,2],[1,3],[3,2],[4,1],[5,2],[3,6]])