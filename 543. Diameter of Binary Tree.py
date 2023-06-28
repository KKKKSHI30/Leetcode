# Depth-first Search Approach:
# Time: O(n)
# Space: O(n)
# 2023.06.26: yes
# notes: 细节问题，返回值，增加长度增加多少等
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_diameter = 0
        def diameter(root):
            if root == None:
                return 0
            left_length = diameter(root.left)
            right_length = diameter(root.right)
            self.max_diameter  = max(self.max_diameter, left_length + right_length)
            return max(left_length, right_length) +1
        diameter(root)
        return self.max_diameter

a = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
b = TreeNode(1, TreeNode(2))
test = Solution()
test.diameterOfBinaryTree(b)
test.diameterOfBinaryTree(a)

