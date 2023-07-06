# Backtracking Approach
# Time: O(2^n*n)
# Space: O(n)
# 2023.07.04: yes
from functools import lru_cache


class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        def backtracking(node, cur_path):
            if node == target:
                results.append(cur_path[:])
                return
            for next_node in graph[node]:
                cur_path.append(next_node)
                backtracking(next_node, cur_path)
                cur_path.pop()
        target = len(graph)-1
        results = []
        backtracking(0, [0])
        return results



# Top-Down Dynamic Programming Approach
# Time: O(2^n*n)
# Space: O(2^n*n)
# 2023.07.04: no
# notes: 并不是很理解这里运用了什么dp的东西，思路感觉和上面差不多，
# 只是for path in all_paths_to_taget(next_node)增加了一步保存的结果
class Solution2(object):
    def allPathsSourceTarget(self, graph):
        target = len(graph) - 1
        # apply the memoization
        @lru_cache(maxsize=None)
        def all_paths_to_target(curr_node):
            if curr_node == target:
                return [[target]]
            results = []
            for next_node in graph[curr_node]:
                for path in all_paths_to_target(next_node):
                    results.append([curr_node] + path)
            return results
        return all_paths_to_target(0)

# Tests:
graph = [[4,3,1],[3,2,4],[3],[4],[]]
test = Solution2()
test.allPathsSourceTarget(graph)