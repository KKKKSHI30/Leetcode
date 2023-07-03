class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# breadth-first Approach
# Time: O(n)
# Space: O(n)
# 2023.07.01: no
class Solution(object):
    def findSecondMinimumValue(self, root):
        self.ans = float('inf')
        min1 = root.val
        def dfs(node):
            if node:
                if min1 < node.val < self.ans:
                    self.ans = node.val
                elif node.val == min1:
                    dfs(node.left)
                    dfs(node.right)
        dfs(root)
        return self.ans if self.ans < float('inf') else -1
# Tests:
tree = TreeNode(2, TreeNode(5), TreeNode(2, TreeNode(3), TreeNode(2)))
tree2 = TreeNode(2, TreeNode(2), TreeNode(2))
test = Solution()
test.findSecondMinimumValue(tree)
test.findSecondMinimumValue(tree2)


