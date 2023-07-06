from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Depth First Search Approach
# Time: O(n)
# Space: O(n)
# 2023.07.04: yes
class Solution:
    def addOneRow(self, root, val, depth):
        if depth == 1:
            return TreeNode(val, root, None)
        elif depth == 2:
            root.left = TreeNode(val, root.left, None)
            root.right = TreeNode(val, None, root.right)
        else:
            if root.left:
                self.addOneRow(root.left, val, depth-1)
            if root.right:
                self.addOneRow(root.right, val, depth-1)
        return root

# Depth First Search with stack Approach
# Time: O(n)
# Space: O(n)
# 2023.07.04: yes
class Solution2:
    class Node:
        def __init__(self, n, d):
            self.node = n
            self.depth = d

    def addOneRow(self, t, v, d) -> TreeNode:
        if d == 1:
            n = TreeNode(v)
            n.left = t
            return n

        stack = []
        stack.append(self.Node(t, 1))
        while stack:
            n = stack.pop()
            if n.node is None:
                continue
            if n.depth == d - 1:
                temp = n.node.left
                n.node.left = TreeNode(v)
                n.node.left.left = temp
                temp = n.node.right
                n.node.right = TreeNode(v)
                n.node.right.right = temp
            else:
                stack.append(self.Node(n.node.left, n.depth + 1))
                stack.append(self.Node(n.node.right, n.depth + 1))
        return t


class Solution3:
    def addOneRow(self, t, v, d):
        if d == 1:
            n = TreeNode(v)
            n.left = t
            return n

        queue = deque()
        queue.append(t)
        depth = 1
        while depth < d - 1:
            temp = deque()
            while queue:
                node = queue.popleft()
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            queue = temp
            depth += 1

        while queue:
            node = queue.popleft()
            temp = node.left
            node.left = TreeNode(v)
            node.left.left = temp
            temp = node.right
            node.right = TreeNode(v)
            node.right.right = temp

        return t


# Test:
tree = TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(1)), TreeNode(6, TreeNode(5)))
test = Solution2()
test.addOneRow(tree, 1, 2)