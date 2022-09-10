# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        check, cur_min, cur_max = self.valid(root)
        return check

    def valid(self, root):
        if root == None:
            return (True, None, None)
        check = True
        cur_min = root.val
        cur_max = root.val
        left_check, left_min, left_max = self.valid(root.left)
        right_check, right_min, right_max = self.valid(root.right)

        if root.left:
            cur_min = min(cur_min, left_min)
            cur_max = max(cur_max, left_max)
        if root.right:
            cur_min = min(cur_min, right_min)
            cur_max = max(cur_max, right_max)

        if left_max != None and (not left_check or left_max >= root.val):
            check = False
        if right_min != None and (not right_check or right_min <= root.val):
            check = False
        return (check, cur_min, cur_max)



node = TreeNode(2, TreeNode(1), TreeNode(3))
node2 = TreeNode(1, TreeNode(2), TreeNode(3))
node3 = TreeNode(2, TreeNode(2), TreeNode(2))
node4 = TreeNode(5, TreeNode(4), TreeNode(6, TreeNode(3), TreeNode(7)))


test = Solution()
result1 = test.isValidBST(node)
result2 = test.isValidBST(node2)
result3 = test.isValidBST(node3)
result4 = test.isValidBST(node4)

class Solution2(object):
    # time complex O(n) and space complex O(n)

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.valid(root, -2 ** 31 - 1, 2 ** 31)

    def valid(self, root, min, max):
        if root == None:
            return True
        if (root != None and root.val <= min) or (root != None and root.val >= max):
            return False
        return self.valid(root.left,min, root.val) and self.valid(root.right, root.val, max)

node = TreeNode(2, TreeNode(1), TreeNode(3))
node2 = TreeNode(1, TreeNode(2), TreeNode(3))
node3 = TreeNode(2, TreeNode(2), TreeNode(2))
node4 = TreeNode(5, TreeNode(4), TreeNode(6, TreeNode(3), TreeNode(7)))


test = Solution2()
result1 = test.isValidBST(node)
result2 = test.isValidBST(node2)
result3 = test.isValidBST(node3)
result4 = test.isValidBST(node4)


class Solution2_5(object):
    # time complex O(n) and space complex O(n)

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.prev = None
        return self.valid(root)

    def valid(self, root):
        if root == None:
            return True
        if (not self.valid(root.left)):
            return False
        if self.prev != None and root.val <= self.prev:
            return False
        self.prev = root.val
        return self.valid(root.right)

node = TreeNode(2, TreeNode(1), TreeNode(3))
node2 = TreeNode(1, TreeNode(2), TreeNode(3))
node3 = TreeNode(2, TreeNode(2), TreeNode(2))
node4 = TreeNode(5, TreeNode(4), TreeNode(6, TreeNode(3), TreeNode(7)))

test = Solution2_5()
result1 = test.isValidBST(node)
result2 = test.isValidBST(node2)
result3 = test.isValidBST(node3)
result4 = test.isValidBST(node4)




class Solution3(object):
    # time
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        values = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            values.append(node.val)
            inorder(node.right)

        inorder(root)

        # Check if the values array is in correct, increasing order
        for i in range(len(values) - 1):
            if values[i] >= values[i + 1]:
                return False
        return True


import math


class Solution4(object):
    # space

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def isBST(node, minn, maxx):
            if not node:
                return True
            else:
                return minn < node.val < maxx and isBST(node.right, node.val, maxx) and isBST(node.left, minn, node.val)

        return isBST(root, -2 ** 31 - 1, 2 ** 31)