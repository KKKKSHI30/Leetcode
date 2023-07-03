class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# breadth-first Approach
# Time: O(n)
# Space: O(n)
# 2023.07.02: yes
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        s = []
        results = []
        if root == None:
            return s
        s.append(root)
        while s:
            max_current = float('-inf')
            current_level = len(s)
            for i in range(current_level):
                node = s.pop(0)
                max_current = max(max_current, node.val)
                if node.right:
                    s.append(node.right)
                if node.left:
                    s.append(node.left)
            results.append(max_current)
        return results

# Tests:
tree = TreeNode(2, TreeNode(5), TreeNode(2, TreeNode(3), TreeNode(2)))
tree2 = TreeNode(2, TreeNode(2), TreeNode(2))
test = Solution()
test.largestValues(tree)