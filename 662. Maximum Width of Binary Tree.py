from collections import deque
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# breadth-first Approach
# Time: O(n)
# Space: O(n)
# 2023.07.01: no
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        max_width = 0
        queue = deque()
        queue.append((root, 0))
        while queue:
            level_length = len(queue)
            _, level_head_index = queue[0]
            # iterate through the current level
            for _ in range(level_length):
                node, col_index = queue.popleft()
                # preparing for the next level
                if node.left:
                    queue.append((node.left, 2 * col_index))
                if node.right:
                    queue.append((node.right, 2 * col_index + 1))
            # calculate the length of the current level,
            #   by comparing the first and last col_index.
            max_width = max(max_width, col_index - level_head_index + 1)
        return max_width


# depth-first Approach
# Time: O(n)
# Space: O(n)
# 2023.07.01: no
class Solution2:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        # table contains the first col_index for each level
        first_col_index_table = {}
        max_width = 0
        def DFS(node, depth, col_index):
            nonlocal max_width
            if node is None:
                return
            # if the entry is empty, set the value
            if depth not in first_col_index_table:
                first_col_index_table[depth] = col_index
            max_width = max(max_width, col_index - first_col_index_table[depth] + 1)
            # Preorder DFS, with the priority on the left child
            DFS(node.left, depth+1, 2*col_index)
            DFS(node.right, depth+1, 2*col_index + 1)
        DFS(root, 0, 0)
        return max_width

# Tests:
tree = TreeNode(1, TreeNode(3, TreeNode(5, TreeNode(6)), None), TreeNode(2, None, TreeNode(9, TreeNode(7))))
test = Solution2()
test.widthOfBinaryTree(tree)