# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import queue
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q = queue.Queue()
        q.put(root)
        depth = 1
        while not q.empty():
            sz = q.qsize()
            for i in range(sz):
                cur = q.get()
                if cur.left == None and cur.right == None:
                    return depth
                if cur.left != None:
                    q.put(cur.left)
                if cur.right != None:
                    q.put(cur.right)
            depth += 1

a = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
test = Solution()
test.minDepth(a)


class Solution2:
    # recursion method
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        children = [root.left, root.right]
        # if we're at leaf node
        if not any(children):
            return 1

        min_depth = float('inf')
        for c in children:
            if c:
                min_depth = min(self.minDepth(c), min_depth)
        return min_depth + 1


class Solution3:
    # dfs iteration
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        else:
            stack, min_depth = [(1, root), ], float('inf')

        while stack:
            depth, root = stack.pop()
            children = [root.left, root.right]
            if not any(children):
                min_depth = min(depth, min_depth)
            for c in children:
                if c:
                    stack.append((depth + 1, c))

        return min_depth