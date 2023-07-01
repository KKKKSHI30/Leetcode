# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursion Approach
# Time: O(logn)
# Space: O(h)
# 2023.06.30: no
# notes: return 的东西是删完的东西，所以一定要赋值
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        def minLeft(root):
            while root.left:
                root = root.left
            return root
        if root == None:
            return None
        if root.val == key:
            if root.left == None:
                return root.right
            elif root.right == None:
                return root.left
            minLeftNode = minLeft(root.right)
            # 删除右树上最小的节点，返回的是删完的右树
            root.right = self.deleteNode(root.right, minLeftNode.val)
            # 也可以直接改值，但是现实情况是最好不要考虑内部的值，所以替换掉比较好
            minLeftNode.left = root.left
            minLeftNode.right = root.right
            root = minLeftNode
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root

# Tests:
tree = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7)))
test = Solution()
result = test.deleteNode(tree, 3)
