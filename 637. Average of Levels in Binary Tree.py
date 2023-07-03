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
    def averageOfLevels(self, root):
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
            current_value = 0
            current_level = len(s)
            for i in range(current_level):
                node = s.pop(0)
                current_value += node.val
                if node.right:
                    s.append(node.right)
                if node.left:
                    s.append(node.left)
            current_value /= current_level
            results.append(current_value)
        return results




# Tests:
tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
tree2 = TreeNode(2, TreeNode(2), TreeNode(2))
test = Solution()
test.averageOfLevels(tree)