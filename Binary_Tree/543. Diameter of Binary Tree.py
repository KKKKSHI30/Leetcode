# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    totalmax = 0

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxdepth(root)
        return self.totalmax

    def maxdepth(self, root):
        if root == None:
            return 0
        leftmax = self.maxdepth(root.left)
        rightmax = self.maxdepth(root.right)
        self.totalmax = max(leftmax+rightmax, self.totalmax)
        return 1+max(leftmax,rightmax)


a = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
b = TreeNode(1, TreeNode(2))
test = Solution()
test.diameterOfBinaryTree(b)
test.diameterOfBinaryTree(a)
