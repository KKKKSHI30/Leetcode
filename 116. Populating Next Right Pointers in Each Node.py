# Level Order Traversal Approach
# Time: O(n)
# Space: O(n)
# 2023.06.26: yes
# notes: 翻转当前和子树
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        saving = [root]
        i, j = 0, 1   # j power, i num of nodes
        while saving:
            cur = saving.pop(0)
            i += 1
            if i == 2 ** j -1:
                j += 1
                cur.next = None
            else:
                cur.next = saving[0]
            if cur.left:
                saving.append(cur.left)
            if cur.right:
                saving.append(cur.right)
        return root

# Level Order Traversal Approach
# Time: O(n)
# Space: O(n)
# 2023.06.26: yes
# notes: same approach as above, but not using perfect tree condition, more general cases
import collections
class Solution2:
    def connect(self, root):

        if not root:
            return root

        Q = collections.deque([root])
        while Q:
            size = len(Q)
            for i in range(size):
                node = Q.popleft()
                if i < size - 1:
                    node.next = Q[0]
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
        return root

# Using previously established next pointers Approach(best approach)
# Time: O(n)
# Space: O(1)
# 2023.06.26: no
# notes: 利用了刚刚建立好的next节点去解决问题
# 有两种connection, 1. 子树的左节点和右节点， 2.子树的右节点和另一个子树的左节点，第二条可以根据1链接好的来链接，还是BFS
class Solution3:
    def connect(self, root):

        if not root:
            return root

        # Start with the root node. There are no next pointers
        # that need to be set up on the first level
        leftmost = root

        # Once we reach the final level, we are done
        while leftmost.left:

            # Iterate the "linked list" starting from the head
            # node and using the next pointers, establish the
            # corresponding links for the next level
            head = leftmost
            while head:

                # CONNECTION 1
                head.left.next = head.right

                # CONNECTION 2
                if head.next:
                    head.right.next = head.next.left

                # Progress along the list (nodes on the current level)
                head = head.next

            # Move onto the next level
            leftmost = leftmost.left

        return root



# Tests:
a = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
test = Solution3()
test.connect(a)



