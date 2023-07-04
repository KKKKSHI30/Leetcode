# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# depth-first Search Approach bottom up
# Time: O(n)
# Space: O(n), when unbalanced
# 2023.07.03: yes
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        def recursion(root, targetSum):
            if root == None:
                return False
            if root.left == None and root.right == None:
                return targetSum - root.val == 0
            left = recursion(root.left, targetSum-root.val)
            right = recursion(root.right, targetSum-root.val)
            return left or right
        return recursion(root, targetSum)

# breadth-first Search Approach bottom up
# Time: O(n)
# Space: O(n), when unbalance
# 2023.07.03: yes
class Solution2:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        de = [(root, sum - root.val), ]
        while de:
            node, curr_sum = de.pop()
            if not node.left and not node.right and curr_sum == 0:
                return True
            if node.right:
                de.append((node.right, curr_sum - node.right.val))
            if node.left:
                de.append((node.left, curr_sum - node.left.val))
        return False

# Tests:
tree = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)), None),
                TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))))
test = Solution()
test.hasPathSum(tree, 22)