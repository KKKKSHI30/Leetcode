# Definition for a binary tree node.
from queue import LifoQueue


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursion Approach
# Time: O(n)
# Space: O(n)
# 2023.06.30: yes
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def traversal(root):
            if root == None:
                return
            traversal(root.left)
            traversal(root.right)
            results.append(root.val)
        results = []
        traversal(root)
        return results

# Iteration Approach
# Time: O(n)
# Space: O(n)
# 2023.06.30: yes
# notes: 弹出当前节点，把当前节点放到results里面，压左压右到stack
# 回归空的时候，弹出收集栈
class Solution2:
    def postorderTraversal(self, root):
        results = []
        post_order_stack = LifoQueue()
        post_order_save_stack = LifoQueue()
        post_order_stack.put(root)
        while (not post_order_stack.empty() and root != None):
            cur = post_order_stack.get()
            post_order_save_stack.put(cur)
            if cur.left:
                post_order_stack.put(cur.left)
            if cur.right:
                post_order_stack.put(cur.right)
        while not post_order_save_stack.empty():
            cur = post_order_save_stack.get()
            results.append(cur.val)
        return results

# Morris Approach:

class Solution3:
    def postorderTraversal(self, root):
        self.result = []
        if root == None:
            return
        cur = root
        while cur != None:
            most_right = cur.left
            if most_right != None:  # there is left tree
                while most_right.right != None and most_right.right != cur:
                    most_right = most_right.right
                if most_right.right == None:
                    most_right.right = cur
                    cur = cur.left
                    continue
                else:
                    most_right.right = None
                    self.print_edge(cur.left)
            cur = cur.right  # no left tree
        self.print_edge(root)
        return self.result


    def print_edge(self, root):
        tail = self.reverse_edge(root)
        cur = tail
        while cur:
            self.result.append(cur.val)
            cur = cur.right
        self.reverse_edge(root)


    def reverse_edge(self, head):
        pre = None
        while head:
            next = head.right
            head.right = pre
            pre = head
            head = next
        return pre

# Tests:
tree = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
test = Solution3()
test.postorderTraversal(tree)