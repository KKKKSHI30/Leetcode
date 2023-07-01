class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursion Approach
# Time: O(n)
# Space: O(n)
# 2023.06.29: yes
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        if root1 == None and root2 == None:
            return None
        elif root1 == None:
            return root2
        elif root2 == None:
            return root1
        root1.val = root1.val + root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1

# Iteration Approach
# Time: O(n)
# Space: O(n)
# 2023.06.29: yes
class Solution2:
    def mergeTrees(self, t1, t2):
        if t1 is None:
            return t2
        stack = [(t1, t2)]
        while stack:
            t = stack.pop()
            if t[0] is None or t[1] is None:
                continue
            t[0].val += t[1].val
            if t[0].left is None:
                t[0].left = t[1].left
            else:
                stack.append((t[0].left, t[1].left))
            if t[0].right is None:
                t[0].right = t[1].right
            else:
                stack.append((t[0].right, t[1].right))
        return t1


# Tests:
a = TreeNode(1, TreeNode(3, TreeNode(5)), TreeNode(2))
b = TreeNode(2, TreeNode(1, None, TreeNode(4)), TreeNode(3, None, TreeNode(7)))
c = TreeNode(1)
d = TreeNode(1, TreeNode(2))
test = Solution()
result = test.mergeTrees(a, b)
result = test.mergeTrees(c,d)
