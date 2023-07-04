# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# depth-first Search Approach (best approach)
# Time: O(n)
# Space: O(d), d is diameter
# 2023.07.03: yes
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def recursion(p, q):
            if p.left and q.left:
                left = recursion(p.left, q.left)
            elif p.left or q.left:
                left = False
            else:
                left = True
            if p.right and q.right:
                right = recursion(p.right, q.right)
            elif p.right or q.right:
                right = False
            else:
                right = True
            if p.val == q.val:
                cur = True
            else:
                cur = False
            return left and right and cur
        if p == None and q == None:
            return True
        elif p and q:
            return recursion(p, q)
        else:
            return False

# depth-first Search Approach (best approach)
# Time: O(n)
# Space: O(d), d is diameter
# 2023.07.03: yes
# notes: 一样的方法和上面就是写的简单点
class Solution2:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # p and q are both None
        if not p and not q:
            return True
        # one of p and q is None
        if not q or not p:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.right, q.right) and \
               self.isSameTree(p.left, q.left)


from collections import deque
# breadth-first Search Approach (best approach)
# Time: O(n)
# Space: O(d), d is diameter
# 2023.07.03: yes
class Solution3:
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

# Tests:
a = TreeNode(1,
             TreeNode(3, TreeNode(4), TreeNode(5)),
             TreeNode(3, TreeNode(6), TreeNode(7))
             )
b = TreeNode(1,
             TreeNode(2, TreeNode(4), TreeNode(5)),
             TreeNode(3, TreeNode(6), TreeNode(7))
             )
test = Solution()
test.isSameTree(a, b)
