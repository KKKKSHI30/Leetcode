class TreeNode(object):
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right

# Recursive Approach
# Time: O(n)
# Space: O(n)
# 2023.07.02: no
# notes: 是个236的改版，只是需要多加一部，找到q和p，而且必须全部遍历
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        found = {'foundP': False, 'foundQ': False}
        res = self.find(root, p.val, q.val, found)
        if not found['foundP'] or not found['foundQ']:
            return None
        return res

    def find(self, root, val1, val2, found):
        if root is None:
            return None

        left = self.find(root.left, val1, val2, found)
        right = self.find(root.right, val1, val2, found)

        if left is not None and right is not None:
            return root

        if root.val == val1:
            found['foundP'] = True
        elif root.val == val2:
            found['foundQ'] = True

        return root if root.val == val1 or root.val == val2 else left or right

# Depth First Search - 2/3 Conditions Approach
# Time: O(n)
# Space: O(n)
# 2023.07.02: no
# notes: 惊为天人，三个条件达成两个即可，1. node是p或者q， 2. p或者q在left tree， 3. p或者q在right tree
# 如果达成就返回，如果没打成就返回左边或者右边，因为左边可能达成了，或者右边可能达成了
# 回到root都没有就是None
class Solution2:
    def lowestCommonAncestor(self, root, p, q):
        self.nodes_found = False

        def dfs(node):
            if not node:
              return node
            left, right = dfs(node.left), dfs(node.right)
            conditions = 0
            if node in (p, q):
              conditions += 1
            if left:
              conditions += 1
            if right:
              conditions += 1
            if conditions == 2:
              self.nodes_found = True

            if (left and right) or node in (p, q): return node
            return left or right

        ans = dfs(root)
        return ans if self.nodes_found else None

# Tests:
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = p = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = q = TreeNode(7)
root.left.right.right = TreeNode(4)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)


test = Solution2()
result = test.lowestCommonAncestor(root, p, q)