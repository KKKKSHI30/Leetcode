# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# depth-first Search Approach
# Time: O(n)
# Space: O(n)
# 2023.07.03: yes
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def recursion(root, add):
            if not root:
                return
            if root.left == None and root.right == None:
                if add:
                    self.total += root.val
                return
            recursion(root.left, True)
            recursion(root.right, False)
        self.total = 0
        recursion(root, False)
        return self.total

# breadth-first Search Approach
# Time: O(n)
# Space: O(n)
# 2023.07.03: yes
class Solution2:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None:
            return 0
        def is_leaf(node):
            return node is not None and node.left is None and node.right is None
        stack = [root]
        total = 0
        while stack:
            sub_root = stack.pop()
            if is_leaf(sub_root.left):
                total += sub_root.left.val
            if sub_root.right is not None:
                stack.append(sub_root.right)
            if sub_root.left is not None:
                stack.append(sub_root.left)
        return total


# Morris Approach
# Time: O(n)
# Space: O(1)
# 2023.07.03: no
class Solution3:
    def sumOfLeftLeaves(self, root):
        total_sum = 0
        current_node = root
        while current_node is not None:
            # If there is no left child, we can simply explore the right subtree
            # without needing to worry about keeping track of currentNode's other
            # child.
            if current_node.left is None:
                current_node = current_node.right
            else:
                previous = current_node.left
                # Check if this left node is a leaf node.
                if previous.left is None and previous.right is None:
                    total_sum += previous.val
                # Find the inorder predecessor for currentNode.
                while previous.right is not None and previous.right is not current_node:
                    previous = previous.right
                # We've not yet visited the inorder predecessor. This means that we
                # still need to explore currentNode's left subtree. Before doing this,
                # we will put a link back so that we can get back to the right subtree
                # when we need to.
                if previous.right is None:
                    previous.right = current_node
                    current_node = current_node.left
                    # We have already visited the inorder predecessor. This means that we
                # need to remove the link we added, and then move onto the right
                # subtree and explore it.
                else:
                    previous.right = None
                    current_node = current_node.right
        return total_sum


# Tests:
tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
tree2 = TreeNode(1)
test = Solution3()
test.sumOfLeftLeaves(tree)
