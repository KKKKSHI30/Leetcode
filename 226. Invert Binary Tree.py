# Recursive Approach:
# Time: O(n)
# Space: O(h) h is the depth of the tree
# 2023.06.26: yes
# notes: 翻转当前和子树
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

# Iterative Approach
# Time: O(n)
# Space: O(n) h is the depth of the tree
# 2023.06.26: yes
# notes: 翻转当前节点，然后把子树上没翻转的节点都放到queue里面去


class Solution2(object):
    def invertTree(self, root):
        if not root:
            return root
        saving = [root]
        while saving:
            cur = saving.pop(-1)
            cur.left, cur.right = cur.right, cur.left
            if cur.left:
                saving.append(cur.left)
            if cur.right:
                saving.append(cur.right)
        return root




# Tests:
a = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
test = Solution()
a_change = test.invertTree(a)
