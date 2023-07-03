class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

# breadth-first Approach
# Time: O(n)
# Space: O(n)
# 2023.07.01: yes
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []
        if root == None:
            return levels
        q = [root]
        level = 0
        while q:
            levels.append([])
            level_length = len(q)
            for i in range(level_length):
                node = q.pop(0)
                levels[level].append(node.val)
                if node.children != None:
                    for child in node.children:
                        q.append(child)
            level += 1
        return levels

# depth-first Approach
# Time: O(n)
# Space: O(n)
# 2023.07.01: yes
class Solution2(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        levels = []
        if root == None:
            return levels
        def recursion(root, level):
            if level == len(levels):
                levels.append([])
            levels[level].append(root.val)
            if root.children:
                for child in root.children:
                    recursion(child, level+1)
        recursion(root, 0)
        return levels

# Tests:
tree = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
test = Solution2()
test.levelOrder(tree)

