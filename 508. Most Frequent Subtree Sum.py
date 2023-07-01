class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Post-Order Recursion Approach (best approach)
# Time: O(n)
# Space: O(n)
# 2023.06.29: yes
class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def frequentSum(root):
            if root == None:
                return 0
            left_sum = frequentSum(root.left)
            right_sum = frequentSum(root.right)
            temp_sum = left_sum+right_sum+root.val
            self.frquency_map[temp_sum] = self.frquency_map.get(temp_sum, 0)+1
            return temp_sum

        self.frquency_map = {}
        frequentSum(root)
        max_value = max(self.frquency_map.values())
        keys_with_max_value = [key for key, value in self.frquency_map.items() if value == max_value]
        return keys_with_max_value

# Pre-Order Recursion Approach
# Time: O(n^2)
# Space: O(n)
# 2023.06.29: no
# notes: 非常复杂，一只重复根本没必要
class Solution2:
    def findFrequentTreeSum(self, root):
        self.sum_freq = {}
        self.max_freq = 0

        def find_tree_sum(root):
            if not root:
                return 0
            # Current root's tree's sum.
            return root.val + find_tree_sum(root.left) + find_tree_sum(root.right)

        def pre_order_traversal(root):
            if not root:
                return

            # Find current node's tree's sum.
            curr_sum = find_tree_sum(root)
            self.sum_freq[curr_sum] = self.sum_freq.get(curr_sum, 0) + 1
            self.max_freq = max(self.max_freq, self.sum_freq[curr_sum])

            # Iterate on left and right subtrees and find their sums.
            pre_order_traversal(root.left)
            pre_order_traversal(root.right)

        # Traverse on all nodes one by one, and find it's tree's sum.
        pre_order_traversal(root)
        max_freq_sums = []
        for sum in self.sum_freq:
            if self.sum_freq[sum] == self.max_freq:
                max_freq_sums.append(sum)

        return max_freq_sums

# Tests:
a = TreeNode(5, TreeNode(2), TreeNode(-3))
b = TreeNode(5, TreeNode(2), TreeNode(-5))
test = Solution()
test.findFrequentTreeSum(a)
test.findFrequentTreeSum(b)


