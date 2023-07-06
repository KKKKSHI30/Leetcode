# Using Node Indegree Approach
# Time: O(v+e)
# Space: O(v+e)
# 2023.07.04: yes
from collections import deque

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        indegree = [0] * numCourses
        graph = [[] for _ in range(numCourses)]
        for i in prerequisites:
            graph[i[1]].append(i[0])
            indegree[i[0]] += 1
        self.onPath = []
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        while queue:
            node = queue.popleft()
            self.onPath.append(node)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        if len(self.onPath) == numCourses:
            return self.onPath
        return []

# Using Depth First Search Approach
# Time: O(v+e)
# Space: O(v+e)
# 2023.07.04: no
from collections import defaultdict
class Solution2:

    WHITE = 1
    GRAY = 2
    BLACK = 3

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        # Create the adjacency list representation of the graph
        adj_list = defaultdict(list)

        # A pair [a, b] in the input represents edge from b --> a
        for dest, src in prerequisites:
            adj_list[src].append(dest)

        topological_sorted_order = []
        is_possible = True

        # By default all vertces are WHITE
        color = {k: Solution2.WHITE for k in range(numCourses)}
        def dfs(node):
            nonlocal is_possible

            # Don't recurse further if we found a cycle already
            if not is_possible:
                return

            # Start the recursion
            color[node] = Solution2.GRAY

            # Traverse on neighboring vertices
            # 如果遇到白色的点，继续遍历因为没遇到过，遇到灰色的点，形成环了，黑色的点，结束过了，不影响任何
            if node in adj_list:
                for neighbor in adj_list[node]:
                    if color[neighbor] == Solution2.WHITE:
                        dfs(neighbor)
                    elif color[neighbor] == Solution.GRAY:
                         # An edge to a GRAY vertex represents a cycle
                        is_possible = False

            # Recursion ends. We mark it as black
            color[node] = Solution2.BLACK
            topological_sorted_order.append(node)

        for vertex in range(numCourses):
            # If the node is unprocessed, then call dfs on it.
            if color[vertex] == Solution2.WHITE:
                dfs(vertex)

        return topological_sorted_order[::-1] if is_possible else []



# Tests:
test = Solution()
test.findOrder(numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]])
test.findOrder(numCourses = 4, prerequisites = [[1,0],[2,3],[3,1],[3,2]])
test.findOrder(numCourses = 2, prerequisites = [[1,0]])
test.findOrder(numCourses = 1, prerequisites = [])
