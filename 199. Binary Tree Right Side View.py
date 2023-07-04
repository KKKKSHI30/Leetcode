from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# breadth-first Search Approach (best approach)
# Time: O(n)
# Space: O(d), d is diameter
# 2023.07.03: yes
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        results = []
        if root == None:
            return results
        q = [root]
        while q:
            level_length = len(q)
            for i in range(level_length):
                node = q.pop(0)
                if i == level_length-1:
                    results.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return results

# depth-first Search Approach (beset approach)
# Time: O(n)
# Space: O(h), h is height
# 2023.07.03: yes
class Solution2:
    def rightSideView(self, root):
        if root is None:
            return []

        rightside = []

        def helper(node, level):
            if level == len(rightside):
                rightside.append(node.val)
            for child in [node.right, node.left]:
                if child:
                    helper(child, level + 1)

        helper(root, 0)
        return rightside

# BFS: One Queue + Sentinel（不如前两个方法好）
# Time: O(n)
# Space: O(d), d is diameter
# 2023.07.03: yes
class Solution3:
    def rightSideView(self, root: TreeNode):
        if root is None:
            return []

        queue = deque([root, None, ])
        rightside = []

        curr = root
        while queue:
            prev, curr = curr, queue.popleft()

            while curr:
                # add child nodes in the queue
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

                prev, curr = curr, queue.popleft()

            # the current level is finished
            # and prev is its rightmost element
            rightside.append(prev.val)
            # add a sentinel to mark the end
            # of the next level
            if queue:
                queue.append(None)

        return rightside

# BFS: Two Queues（不如前三个方法好）
# Time: O(n)
# Space: O(d), d is diameter
# 2023.07.03: yes
class Solution4:
    def rightSideView(self, root):
        if root is None:
            return []

        next_level = deque([root, ])
        rightside = []

        while next_level:
            # prepare for the next level
            curr_level = next_level
            next_level = deque()

            while curr_level:
                node = curr_level.popleft()

                # add child nodes of the current level
                # in the queue for the next level
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            # The current level is finished.
            # Its last element is the rightmost one.
            rightside.append(node.val)

        return rightside

# Tests:
tree = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
test = Solution2()
test.rightSideView(tree)






