# Definition for a binary tree node.
from queue import Queue


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        return self.breath_first(root, 1)

    def breath_first(self, root, num):
        """Width traversal"""
        q = Queue()
        cur = root
        q.put(cur)
        while (cur != None and not q.empty()):
            cur = q.get()
            print(cur.element)
            if cur.left:
                q.put(cur.left)
            if cur.right:
                q.put(cur.right)


