# Depth First Search Approach
# Time: O(m+n)
# Space: O(n)
# 2023.07.04: yes
from collections import deque

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        def traverse(graph, s):
            if self.onPath[s]:
                self.hasCycle = True
            # 这里用visited的意思是，这个点以前走过了，所以他的后续以前也走过了，不要重复运算了
            # hasCycle的话就直接返回就行了，已经有环了
            if self.visited[s] or self.hasCycle:
                return
            self.visited[s] = True
            self.onPath[s] = True
            for t in graph[s]:
                traverse(graph, t)
            self.onPath[s] = False

        graph = [[] for _ in range(numCourses)]
        for edge in prerequisites:
            graph[edge[1]].append(edge[0])
        self.visited = [False] * numCourses
        self.onPath = [False] * numCourses
        self.hasCycle = False
        for i in range(numCourses):
            traverse(graph, i)
        return not self.hasCycle

# Topological Sort Using Kahn's Algorithm Approach
# Time: O(m+n)
# Space: O(m+n)
# 2023.07.04: yes
class Solution2:
    def canFinish(self, numCourses, prerequisites):
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        # 构建图
        for prerequisite in prerequisites:
            adj[prerequisite[1]].append(prerequisite[0])
            indegree[prerequisite[0]] += 1
        # 找到没有in_degree的nodes，从他们开始
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        nodesVisited = 0
        while queue:
            node = queue.popleft()
            nodesVisited += 1
            # 把与之相关联的nodes入度减一，如果入度为0，加到queue里面去
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return nodesVisited == numCourses

# Tests:
test = Solution()
test.canFinish(numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]])
test.canFinish(numCourses = 2, prerequisites = [[1,0]])
test.canFinish(numCourses = 2, prerequisites = [[1,0],[0,1]])