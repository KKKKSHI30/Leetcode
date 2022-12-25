# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q == None:
            return True
        elif p == None and q != None:
            return False
        elif q == None and p != None:
            return False
        if p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

a = TreeNode(1,
             TreeNode(2, TreeNode(4), TreeNode(5)),
             TreeNode(3, TreeNode(6), TreeNode(7))
             )
b = TreeNode(1,
             TreeNode(3, TreeNode(4), TreeNode(5)),
             TreeNode(3, TreeNode(6), TreeNode(7))
             )
test = Solution()
test.isSameTree(a, b)

from collections import deque
class Solution2:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def check(p, q):
            # if both are None
            if not p and not q:
                return True
            # one of p and q is None
            if not q or not p:
                return False
            if p.val != q.val:
                return False
            return True
        deq = deque([(p, q), ])
        while deq:
            p, q = deq.popleft()
            if not check(p, q):
                return False
            if p:
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))
        return True

test2 = Solution2()
test2.isSameTree(a, b)
