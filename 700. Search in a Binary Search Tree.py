class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursive Algorithm (best approach)
# Time: O(h)
# Space: O(h)
# 2023.06.29: yes
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        def dfs(root, val):
            if root == None:
                return None
            if val == root.val:
                return root
            if val < root.val:
                left = dfs(root.left, val)
                if left != None:
                    return left
            if val > root.val:
                right = dfs(root.right, val)
                if right != None:
                    return right
        return dfs(root, val)

# Iteration Algorithm (best approach)
# Time: O(h)
# Space: O(1)
# 2023.06.29: yes
class Solution2:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root is not None and root.val != val:
            root = root.left if val < root.val else root.right
        return root

# Tests:
tree = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
test = Solution()
a = test.searchBST(tree,2)