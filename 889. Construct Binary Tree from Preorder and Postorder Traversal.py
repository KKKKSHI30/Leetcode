# Recursion Approach
# Time: O(n)
# Space: O(n)
# 2023.06.27: yes

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def constructFromPrePost(self, preorder, postorder):
        """
        :type preorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        self.preorder_index = 0

        postorder_index_map = {}
        for index, value in enumerate(postorder):
            postorder_index_map[value] = index

        def array_to_tree(left, right):
            if left > right: return None
            root_value = preorder[self.preorder_index]
            root = TreeNode(root_value)
            self.preorder_index += 1
            if left == right:
                return root
            bound = preorder[self.preorder_index]
            bound2 = postorder_index_map[bound]
            root.left = array_to_tree(left, bound2)
            root.right = array_to_tree(bound2+ 1, right-1)

            return root
        return array_to_tree(0, len(postorder) - 1)

# Tests:
test = Solution()
a = test.constructFromPrePost(preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1])
b = test.constructFromPrePost(preorder = [1], postorder = [1])
c = test.constructFromPrePost(preorder = [1,2,3], postorder = [3,2,1])