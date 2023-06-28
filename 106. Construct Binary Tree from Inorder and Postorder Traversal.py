# Recursion Approach
# Time: O(n)
# Space: O(n)
# 2023.06.27: yes
# notes: 根据105改的，postorder是从右往左，因为是从右往左Process
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        self.postorder_index = len(postorder) -1
        inorder_index_map = {}
        for index, value in enumerate(inorder):
            inorder_index_map[value] = index

        def array_to_tree(left, right):
            if left > right: return None
            root_value = postorder[self.postorder_index]
            root = TreeNode(root_value)
            self.postorder_index -= 1
            root.right = array_to_tree(inorder_index_map[root_value] + 1, right)
            root.left = array_to_tree(left, inorder_index_map[root_value] - 1)
            return root
        return array_to_tree(0, len(postorder) - 1)

# Tests:
test = Solution()
a = test.buildTree(inorder = [9,3,15,20,7], postorder = [9,15,7,20,3])