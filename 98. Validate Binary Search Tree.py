import math
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursive Traversal with Valid Range Algorithm (best approach)
# Time: O(n)
# Space: O(n)
# 2023.06.29: yes
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def valid(root, min, max):
            if root == None:
                return True
            if root.val >= max or root.val <= min:
                return False
            left_valid = valid(root.left, min, root.val)
            right_valid = valid(root.right, root.val, max)
            return left_valid and right_valid

        return valid(root, float('-inf'), float('inf'))


# Iterative Traversal with Valid Range Algorithm (best approach)
# Time: O(n)
# Space: O(n)
# 2023.06.29: yes
class Solution2:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        stack = [(root, -math.inf, math.inf)]
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            val = root.val
            if val <= lower or val >= upper:
                return False
            stack.append((root.right, val, upper))
            stack.append((root.left, lower, val))
        return True

# Recursive Inorder Traversal Algorithm (best approach)
# Time: O(n)
# Space: O(n)
# 2023.06.29: yes
class Solution3:
    def isValidBST(self, root: TreeNode) -> bool:

        def inorder(root):
            if not root:
                return True
            if not inorder(root.left):
                return False
            if root.val <= self.prev:
                return False
            self.prev = root.val
            return inorder(root.right)

        self.prev = -math.inf
        return inorder(root)

# Iterative Inorder Traversal
# Time: O(n)
# Space: O(n)
# 2023.06.29: yes
class Solution4:
    def isValidBST(self, root: TreeNode) -> bool:
        stack, prev = [], -math.inf

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # If next element in inorder traversal
            # is smaller than the previous one
            # that's not BST.
            if root.val <= prev:
                return False
            prev = root.val
            root = root.right
        return True


# Tests:
tree = TreeNode(10, TreeNode(5), TreeNode(15, TreeNode(6), TreeNode(20)))
test = Solution()
test.isValidBST(tree)
