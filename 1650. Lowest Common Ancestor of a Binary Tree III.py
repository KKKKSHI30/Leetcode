class TreeNode(object):
    def __init__(self, x, left = None, right = None, parent = None):
        self.val = x
        self.left = left
        self.right = right
        self.parent = parent

# Iterative Approach
# Time: O(n)
# Space: O(n)
# 2023.07.02: yes
class Solution:
    def lowestCommonAncestor(self, p, q):
        path = set()
        while p:
            path.add(p)
            p = p.parent
        while q not in path:
            q = q.parent
        return q

# notes: 就是单链表结构，看pq的共同节点是谁， p接q,q接p，如果有一样的公共节点一定会遇到，不然就是头结点
class Solution2:
    def lowestCommonAncestor(self, p, q):
        p1, p2 = p, q
        while p1 != p2:
            p1 = p1.parent if p1.parent else q
            p2 = p2.parent if p2.parent else p
        return p1


# Tests:
tree = TreeNode(3)
tree.left = TreeNode(5)
tree.right = p = TreeNode(1)

tree.left.left  = TreeNode(6)
tree.left.left.parent = tree.left
tree.left.right = TreeNode(2)
tree.left.right.parent = tree.left
tree.left.parent = tree

tree.right.left = TreeNode(0)
tree.right.left.parent = tree.right
tree.right.right = q= TreeNode(8)
tree.right.right.parent = tree.right
tree.right.parent = tree

test = Solution2()
result = test.lowestCommonAncestor(p, q)









