# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Breadth-first Search
# Time: O(n)
# Space: O(d), d is diameter
# 2023.07.03: yes
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        q = [root]
        level = 1
        while q:
            level_length = len(q)
            for i in range(level_length):
                node = q.pop(0)
                if node.left == None and node.right == None:
                    return level
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level +=1
        return level

# Tests:
tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
tree2 = TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5, None, TreeNode(6)))))
result = Solution()
result.minDepth(tree2)


