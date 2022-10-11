# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from queue import Queue
from queue import LifoQueue
from collections import deque

class Solution(object):
    # wrong version
    def zigzagLevelOrder_wrong(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q = Queue()
        q.put(root)
        reverse = False
        while not q.empty():
            cur = q.get()
            print(cur.val)
            if reverse:
                if cur.left:
                    q.put(cur.left)
                if cur.right:
                    q.put(cur.right)
            else:
                if cur.right:
                    q.put(cur.right)
                if cur.left:
                    q.put(cur.left)
            reverse = not reverse


class Solution2:
    # 看python node Tree的第九条
    # bfs方法，优先考虑这个方法
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        level_list = deque()
        if root is None:
            return []
        # start with the level 0 with a delimiter
        node_queue = deque([root, None])
        is_order_left = True

        while len(node_queue) > 0:
            curr_node = node_queue.popleft()

            if curr_node:
                if is_order_left:
                    level_list.append(curr_node.val)
                else:
                    level_list.appendleft(curr_node.val)

                if curr_node.left:
                    node_queue.append(curr_node.left)
                if curr_node.right:
                    node_queue.append(curr_node.right)
            else:
                # we finish one level
                ret.append(level_list)
                # add a delimiter to mark the level
                if len(node_queue) > 0:
                    node_queue.append(None)

                # prepare for the next level
                level_list = deque()
                is_order_left = not is_order_left

        return ret


from collections import deque

class Solution3:
    # dfs方法，有点强硬，but it's ok
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        results = []
        def dfs(node, level):
            if level >= len(results):
                results.append(deque([node.val]))
            else:
                if level % 2 == 0:
                    results[level].append(node.val)
                else:
                    results[level].appendleft(node.val)

            for next_node in [node.left, node.right]:
                if next_node is not None:
                    dfs(next_node, level+1)

        # normal level order traversal with DFS
        dfs(root, 0)

        return results


class Solution4(object):
    # 常规dfs，优化版
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        self.helper(root, ans, 0)
        self.zigzag(ans)
        return ans

    def helper(self, root, ans, order):
        if root is None:
            return
        if len(ans) < order + 1:
            ans.append([])

        ans[order].append(root.val)

        self.helper(root.left, ans, order + 1)
        self.helper(root.right, ans, order + 1)

    def zigzag(self, ans):
        row = 1
        while row < len(ans):
            ans[row].reverse()
            row += 2

class Solution5(object):
    # 常规bfs，优化版，不需要分隔符，直接用Len来确定
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        q = deque([root])
        res = []
        direct = 0
        while q:
            q_len = len(q)
            level_list = []
            direct += 1
            for i in range(q_len):
                node = q.popleft()
                level_list.append(node.val)
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
            if (direct % 2) == 1:
                level_list = level_list[::-1]
            res.append(level_list)
        return res

tree1 = TreeNode(1,
             TreeNode(2, TreeNode(4), TreeNode(5)),
             TreeNode(3, TreeNode(6), TreeNode(7))
             )

result = Solution5()
t1 = result.zigzagLevelOrder(tree1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
