class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Depth First Search Approach
# Time: O(n)
# Space: O(n)
# 2023.07.04: yes

class Solution:
    def findTarget(self, root, k):
        def inorder(root, values):
            if root is None:
                return
            inorder(root.left, values)
            values.append(root.val)
            inorder(root.right, values)

        values = []
        inorder(root, values)
        left, right = 0, len(values) - 1
        while left < right:
            total = values[left] + values[right]
            if total == k:
                return True
            elif total < k:
                left += 1
            else:
                right -= 1
        return False


# Tests:
tree = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7)))
test = Solution()
test.findTarget(tree, 8)
