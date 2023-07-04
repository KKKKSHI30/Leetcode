# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# depth-first Search Approach bottom up
# Time: O(n)
# Space: O(n), when unbalanced
# 2023.07.03: yes
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        def recursion(root, targetSum, cur):
            if root == None:
                return
            if root.left == None and root.right == None:
                if targetSum - root.val == 0:
                    cur.append(root.val)
                    results.append(cur[:])
                    cur.pop()
                    return
                else:
                    return
            cur.append(root.val)
            recursion(root.left, targetSum-root.val, cur)
            recursion(root.right, targetSum-root.val, cur)
            cur.pop()
        results = []
        recursion(root, targetSum, [])
        return results


# Tests:
tree = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)), None),
                TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1))))
test = Solution()
test.pathSum(tree, 22)








