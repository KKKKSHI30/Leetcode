# Recursion Approach
# Time: O(n^2)
# Space: O(n)
# 2023.06.27: no
# notes: 确认当前array最大节点，构造节点，然后左边就是node.left,右边就是node.right，根据递归，左边的Node.left也是左边array最大值
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def constuct(nums, low, high):
            if low > high:
                return None
            ind, maxValue = -1, float('-inf')
            for i in range(low, high + 1):
                if maxValue < nums[i]:
                    ind = i
                    maxValue = nums[i]
            root = TreeNode(maxValue)
            # 递归调用构造左右子树
            root.left = constuct(nums, low, ind - 1)
            root.right = constuct(nums, ind + 1, high)
            return root

        root = constuct(nums, 0, len(nums)-1)
        return root

# Tests:
test = Solution()
test.constructMaximumBinaryTree([3,2,1,6,0,5])