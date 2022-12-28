# Definition for a binary tree node.
from queue import LifoQueue


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.saving = []
        self.preorder(root)
        return self.saving

    def preorder(self, root):
        if root == None:
            return
        self.saving.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

class Solution2(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.saving = []
        pre_order_stack = LifoQueue()
        if root == None:
            return self.saving
        pre_order_stack.put(root)
        while not pre_order_stack.empty():
            cur = pre_order_stack.get()
            self.saving.append(cur.val)
            if cur.right:
                pre_order_stack.put(cur.right)
            if cur.left:
                pre_order_stack.put(cur.left)
        return self.saving


a = TreeNode(3, TreeNode(1), TreeNode(2))
test = Solution2()
c = test.preorderTraversal(None)
b = test.preorderTraversal(a)

class Solution3(object):
    # morris traverse
    def preorderTraversal(self, root):
        saving = []
        if root == None:
            return
        cur = root
        while cur != None:
            most_right = cur.left
            if most_right != None:  # there is left tree
                while most_right.right != None and most_right.right != cur:
                    most_right = most_right.right
                if most_right.right == None:
                    saving.append(cur.val)
                    most_right.right = cur
                    cur = cur.left
                    continue
                else:
                    most_right.right = None
            else:
                saving.append(cur.val)
            cur = cur.right  # no left tree
