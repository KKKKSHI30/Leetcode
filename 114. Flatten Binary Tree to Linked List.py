# Recursion Approach
# Time: O(n)
# Space: O(n)
# 2023.06.26: no
# notes: 重点是在后序位置，作为总结把左右两边拉平之后的结果进行处理
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def flatten(self, root: TreeNode) -> None:
        # base case
        if not root:
            return
        # 利用定义，把左右子树拉平
        self.flatten(root.left)
        self.flatten(root.right)
        # 后序遍历位置
        # 1、左右子树已经被拉平成一条链表
        left = root.left
        right = root.right
        # 2、将左子树作为右子树
        root.left = None
        root.right = left
        # 3、将原先的右子树接到当前右子树的末端
        p = root
        while p.right:
            p = p.right
        p.right = right


# Iterative Solution using Stack Approach
# Time: O(n)
# Space: O(n)
# 2023.06.26: no
# notes: 有两个状态，start,end，end表示至少左树已经排序好，start说明需要排序，如果start有左树，就把头结点改为end，再把左树头压进栈
# 因为左树先pop出来，排序好后，头结点就没有左树，自然是end，如果start没有左树，直接压进右树
# 如果没进尾节点之前，就没有tailnode，这时候只能不断压没有排序好的栈，直到有了尾节点之后，倒着连上去
# 剩下的就是连接头尾，靠stack的方式从尾到头排序，同时还要确定tail是什么，tail的右树要接头结点的右树
import collections

class Solution2:

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        # Handle the null scenario
        if not root:
            return None

        START, END = 1, 2

        tailNode = None
        stack = collections.deque([(root, START)])

        while stack:

            currentNode, recursionState = stack.pop()

            # We reached a leaf node. Record this as a tail
            # node and move on.
            if not currentNode.left and not currentNode.right:
                tailNode = currentNode
                continue

            # If the node is in the START state, it means we still
            # haven't processed it's left child yet.
            if recursionState == START:

                # If the current node has a left child, we add it
                # to the stack AFTER adding the current node again
                # to the stack with the END recursion state.
                if currentNode.left:
                    stack.append((currentNode, END))
                    stack.append((currentNode.left, START))
                elif currentNode.right:

                    # In case the current node didn't have a left child
                    # we will add it's right child
                    stack.append((currentNode.right, START))
            else:
                # If the current node is in the END recursion state,
                # that means we did process one of it's children. Left
                # if it existed, else right.
                rightNode = currentNode.right

                # If there was a left child, there must have been a leaf
                # node and so, we would have set the tailNode
                if tailNode:
                    # Establish the proper connections.
                    tailNode.right = currentNode.right
                    currentNode.right = currentNode.left
                    currentNode.left = None
                    rightNode = tailNode.right

                if rightNode:
                    stack.append((rightNode, START))

# O(1) Iterative Solution Approach
# Time: O(n)
# Space: O(1)
# 2023.06.26: no
# notes: 非常像morris遍历，如果有左树，找出左树的最右节点（他没有右树，但是可以有左树），把头结点的右树，接到这个的右树上面
# 因此头结点没有右树，只有左树；把左树变成右树，遍历下一个节点，重复，如果有左树，同样的过程，没有左树，直接进右节点

class Solution3:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Handle the null scenario
        if not root:
            return None
        node = root
        while node:
            # If the node has a left child
            if node.left:
                # Find the rightmost node
                rightmost = node.left
                while rightmost.right:
                    rightmost = rightmost.right
                # rewire the connections
                rightmost.right = node.right
                node.right = node.left
                node.left = None
            # move on to the right side of the tree
            node = node.right

# Tests:
r = TreeNode(5)
r.left = TreeNode(2)
r.left.right = TreeNode(6)
r.left.right.left = TreeNode(44)
r.left.right.left.right = TreeNode(23)
r.right = TreeNode(1)
r.right.left = TreeNode(10)
r.right.right = TreeNode(11)

test = Solution2()
test.flatten(r)
