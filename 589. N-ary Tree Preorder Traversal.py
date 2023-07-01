class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

# Recursion Approach
# Time: O(nlok)
# Space: O(logk)
# 2023.06.30: yes
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        def dfs(root):
            if root == None:
                return
            self.result.append(root.val)
            if root.children == None:
                return
            for child in root.children:
                dfs(child)
        self.result = []
        dfs(root)
        return self.result

# Iterations Approach
# Time: O(nlok)
# Space: O(logk)
# 2023.06.30: yes

class Solution2(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []
        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            output.append(root.val)
            stack.extend(root.children[::-1])
        return output

# Tests:
tree = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
test = Solution2()
test.preorder(tree)