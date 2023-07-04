# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# depth-first Search Approach bottom up
# Time: O(n)
# Space: O(d), d is diameter
# 2023.07.03: yes
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def recursion(root):
            if root == None:
                return None
            left_result = recursion(root.left)
            right_result = recursion(root.right)
            if left_result != None and right_result != None:
                self.max_value = max(left_result, right_result, left_result+right_result+root.val,
                                     max(left_result,right_result)+root.val, root.val,
                                     self.max_value)
                return max(max(left_result, right_result) + root.val, root.val)
            elif left_result == None and right_result:
                self.max_value = max(right_result, right_result + root.val, root.val, self.max_value)
                return max(right_result + root.val, root.val)
            elif right_result == None and left_result:
                self.max_value = max(left_result, left_result + root.val, root.val, self.max_value)
                return max(left_result + root.val, root.val)
            else:
                self.max_value = max(root.val, self.max_value)
                return root.val
        self.max_value = float("-inf")
        recursion(root)
        return self.max_value

# depth-first Search Approach bottom up(best approach)
# Time: O(n)
# Space: O(d), d is diameter
# 2023.07.03: yes
# notes: 方法一样，但是写的更简单，trick就是，永远不加0以下的东西
class Solution2:
    def maxPathSum(self, root):
        max_path = -float('inf')
        def gain_from_subtree(node):
            nonlocal max_path
            if not node:
                return 0
            gain_from_left = max(gain_from_subtree(node.left), 0)
            gain_from_right = max(gain_from_subtree(node.right), 0)
            max_path = max(max_path, gain_from_left + gain_from_right + node.val)
            return max(
                gain_from_left + node.val,
                gain_from_right + node.val
            )

        gain_from_subtree(root)
        return max_path
# Tests:
tree5 = TreeNode(2, TreeNode(-1), TreeNode(-2))
tree4 = TreeNode(1, TreeNode(-2), TreeNode(3))
tree3 = TreeNode(2, TreeNode(-1))
tree2 = TreeNode(-3)
tree = TreeNode(-2, TreeNode(-3, TreeNode(2), TreeNode(-1)), TreeNode(5, TreeNode(1), TreeNode(2)))
test = Solution2()
test.maxPathSum(tree2)