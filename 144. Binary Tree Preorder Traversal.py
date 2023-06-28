# Recursion Approach:
# Time: O(n)
# Space: O(n)
# 2023.06.26: yes
# Definition for a binary tree node.
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
        results = []

        def preorder(root):
            if root == None:
                return
            results.append(root.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return results


# Iteration Approach:
# Time: O(n)
# Space: O(n)
# 2023.06.26: yes
class Solution2(object):
    def preorderTraversal(self, root):
        results = []
        nodes = []
        if root == None:
            return results
        nodes.append(root)
        while nodes:
            cur = nodes.pop(0)
            results.append(cur.val)
            if cur.left:
                nodes.append(cur.left)
            if cur.right:
                nodes.append(cur.right)
        return results


# Morris Traversal Approach:
# Time: O(n)
# Space: O(1)
# 2023.06.26: no
# notes:
# 当前节点cur
# 1. 如果没有left, cur = cur.tigh
# 2. 如果有left, 找到左树上最右节点mostRight
# 2a. 如果mostRight右指针为空，mostRight.right = cur,然后cur = cur.left
# 2b. 如果mostRight右指针为cur， mostRight.right = None, cur = cur.right
# 3. cur == None的时候停止遍历
class Solution3(object):
    def preorderTraversal(self, root):
        results = []
        if root == None:
            return
        cur = root
        while cur != None:
            most_right = cur.left
            if most_right != None:
                while most_right.right != None and most_right.right != cur:
                    most_right = most_right.right
                if most_right.right == None:
                    results.append(cur.val)
                    most_right.right = cur
                    cur = cur.left
                    continue
                else:
                    most_right.right = None
            else:
                results.append(cur.val)
            cur = cur.right
        return results
# Tests:
a = TreeNode(3, TreeNode(1), TreeNode(2))
test = Solution2()
test.preorderTraversal(a)
test.preorderTraversal(None)
"""
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
"""