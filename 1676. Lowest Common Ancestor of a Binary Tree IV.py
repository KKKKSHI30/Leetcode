class TreeNode(object):
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

# Recursive Approach
# Time: O(n)
# Space: O(n)
# 2023.07.02: yes
class Solution(object):
    def lowestCommonAncestor(self, root, nodes):
        """
        :type root: TreeNode
        :type nodes: List[TreeNode]
        """
        def recursion(root, nodes):
            if root == None:
                return None
            for node in nodes:
                if node.val == root.val:
                    return root
            left = recursion(root.left, nodes)
            right = recursion(root.right, nodes)
            if left != None and right != None:
                return root
            return left if left is not None else right
        return recursion(root, nodes)


# Tests:
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = p = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = q = TreeNode(4)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)


test = Solution()
result = test.lowestCommonAncestor(root, [p,q])