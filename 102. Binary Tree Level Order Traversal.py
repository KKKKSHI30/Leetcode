class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# breadth-first Approach
# Time: O(n)
# Space: O(n)
# 2023.07.01: yes
# notes: double for loop，一个是queue，一个是每一层，进下一层之前，count一下queue就行了
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []
        if root == None:
            return levels
        level = 0
        q = [root]
        while q:
            levels.append([])
            level_length = len(q)
            for i in range(level_length):
                node = q.pop(0)
                levels[level].append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return levels

# depth-first Approach
# Time: O(n^2)
# Space: O(1)
# 2023.07.01: yes
# notes: 需要考虑层数，然后每新的一层建[]
class Solution2(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []
        if root == None:
            return levels
        def node_recursion(node, level):
            if len(levels) == level:
                levels.append([])
            levels[level].append(node.val)
            if node.left:
                node_recursion(node.left, level+1)
            if node.right:
                node_recursion(node.right, level+1)
        node_recursion(root, 0)
        return levels


# Tests:
tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
test = Solution()
test.levelOrder(tree)






