# Recursion
# Time: O(n)
# Space: O(n)
# 2023.07.28: yes
# notes: 用tuple存储rob和not rob即可
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: TreeNode) -> int:
        def helper(node):
            # return [rob this node, not rob this node]
            if not node:
                return (0, 0)
            left = helper(node.left)
            right = helper(node.right)
            # if we rob this node, we cannot rob its children
            rob = node.val + left[1] + right[1]
            # else we could choose to either rob its children or not
            not_rob = max(left) + max(right)
            return [rob, not_rob]
        return max(helper(root))


# Recursion with Memoization
# Time: O(n)
# Space: O(n)
# 2023.07.28: yes
# notes: 分类存储rob和not rob，如果parent rob了，他的子孩子必须not rob，
# 或者他可以rob或者not rob，他的孩子可以not rob 或者rob/not rob
# rob对应的是not rob; not rob对应的是rob/not rob-> not rob/   rob/not rob
# 还是挺confused，第二个状态其实是随意，取max，第一个状态是子孩子必须不能rob
class Solution2:
    def rob(self, root):
        rob_saved = {}
        not_rob_saved = {}
        def helper(node, parent_robbed):
            if not node:
                return 0
            if parent_robbed:
                if node in rob_saved:
                    return rob_saved[node]
                result = helper(node.left, False) + helper(node.right, False)
                rob_saved[node] = result
                return result
            else:
                if node in not_rob_saved:
                    return not_rob_saved[node]
                rob = node.val + helper(node.left, True) + helper(node.right, True)
                not_rob = helper(node.left, False) + helper(node.right, False)
                result = max(rob, not_rob)
                not_rob_saved[node] = result
                return result
        return helper(root, False)

# Tests:
a = TreeNode(3, TreeNode(2, None, TreeNode(3)), TreeNode(3, None, TreeNode(1)))
test = Solution2()
test.rob(a)


# Dynamic Programming
# Time: O(n)
# Space: O(n)
# 2023.07.28: yes
# notes: 挺清晰的，应该没啥问题，对应上面recursion
class Solution3:
    def rob(self, root):
        if not root:
            return 0
        # reform tree into array-based tree
        tree = []
        graph = {-1: []}
        index = -1
        q = [(root, -1)]
        while q:
            node, parent_index = q.pop(0)
            if node:
                index += 1
                tree.append(node.val)
                graph[index] = []
                graph[parent_index].append(index)
                q.append((node.left, index))
                q.append((node.right, index))
        # represent the maximum start by node i with robbing i
        dp_rob = [0] * (index + 1)
        # represent the maximum start by node i without robbing i
        dp_not_rob = [0] * (index + 1)
        for i in reversed(range(index + 1)):
            if not graph[i]:  # if is leaf
                dp_rob[i] = tree[i]
                dp_not_rob[i] = 0
            else:
                dp_rob[i] = tree[i] + sum(dp_not_rob[child]
                                          for child in graph[i])
                dp_not_rob[i] = sum(max(dp_rob[child], dp_not_rob[child])
                                    for child in graph[i])
        return max(dp_rob[0], dp_not_rob[0])











