class TreeNode(object):
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right

# Recursive Approach
# Time: O(n)
# Space: O(n)
# 2023.07.02: no
# 两个点，1. 因为是求公共节点，所以是需要拿到子节点的结果，才能算出来，所以肯定是后序遍历的改版
# 2. 回归的时候，如果左树有，右树没有，这种情况，肯定两个点都在左树上，返回第一个遇到的左树的root就可以，根本就不需要继续遍历
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def recursion(root, p, q):
            if root == None:
                return None
            if root.val == p.val or root.val == q.val:
                return root
            left = recursion(root.left, p, q)
            right = recursion(root.right, p, q)
            if left != None and right != None:
                return root
            return left if left is not None else right
        return recursion(root, p, q)

# Iterative using parent pointers Approach
# Time: O(n)
# Space: O(n)
# 2023.07.02: no
# notes: 1.每个节点都存储他的父节点，
# 2. 找到pq并且存到hash map里，
# 3. 把p的父节点全部存起来，
# 4. 从q开始找，q在不在p的父节点里，直到找到返回

class Solution2:
    def lowestCommonAncestor(self, root, p, q):
        stack = [root]
        parent = {root: None}
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]
        while q not in ancestors:
            q = parent[q]
        return q

# Iterative without parent pointers Approach
# Time: O(n)
# Space: O(n)
# 2023.07.02: no
# notes: 1. 三个状态的变化，两个nodes都弄完了，弄完了一个，一个都没弄完
# 2. 找到其中一个点之后，记录他在stack的位置，如果找到另一个点的时候，位置不同，就-1，就是找他的父节点，继续确认父节点
class Solution3:
    BOTH_PENDING = 2
    LEFT_DONE = 1
    BOTH_DONE = 0

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        stack = [(root, Solution3.BOTH_PENDING)]
        one_node_found = False
        LCA_index = -1
        while stack:
            parent_node, parent_state = stack[-1]
            if parent_state != Solution3.BOTH_DONE:
                if parent_state == Solution3.BOTH_PENDING:
                    if parent_node == p or parent_node == q:
                        if one_node_found:
                            return stack[LCA_index][0]
                        else:
                            one_node_found = True
                            LCA_index = len(stack) - 1
                    child_node = parent_node.left
                else:
                    child_node = parent_node.right
                stack.pop()
                stack.append((parent_node, parent_state - 1))
                if child_node:
                    stack.append((child_node, Solution3.BOTH_PENDING))
            else:
                if one_node_found and LCA_index == len(stack) - 1:
                    LCA_index -= 1
                stack.pop()
        return None

# Tests:
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = p = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = q = TreeNode(4)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)


test = Solution3()
test.lowestCommonAncestor(root, p, q)