# BST Binary Search Tree: 搜索二叉树
# CBT Complete Binary Tree: 完全二叉树
# FBT: 满二叉树
# Balanced ST: 平衡二叉树：所有左树和右树差最多为1
from queue import Queue

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BST(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.bucket = []
        self.in_order(root)
        for i in range(len(self.bucket) - 1):
            if self.bucket[i] >= self.bucket[i+1]:
                return False
        return True

    def in_order(self, root):
        if root == None:
            return
        self.in_order(root.left)
        self.bucket.append(root.val)
        self.in_order(root.right)

    def isValidBST2(self, root):
        check, min, max = self.valid_BST(root)
        return check

    def valid_BST(self, root):
        if root == None:
            return (True, None, None)
        cur_min = root.val
        cur_max = root.val
        left_check, left_min, left_max = self.valid_BST(root.left)
        right_check, right_min, right_max = self.valid_BST(root.right)

        if root.left != None:
            cur_min = min(cur_min, left_min)
            cur_max = max(cur_max, left_max)
        if root.right != None:
            cur_min = min(cur_min, right_min)
            cur_max = max(cur_max, right_max)
        check = True

        if left_max != None and (not left_check or left_max >= root.val):
            check = False
        if right_min != None and (not right_check or right_min <= root.val):
            check = False
        return (check, cur_min, cur_max)

    def isValidBST3(self, root):
        self.prev = None
        return self.inorder3(root)

    def inorder3(self,root):
        if root == None:
            return True
        if not self.inorder3(root.left):
            return False
        if self.prev != None and root.val < self.prev:
            return False
        self.prev = root.val
        return self.inorder3(root.right)

    def isValidBST4(self, root):
        return self.validate4(root, None, None)

    def validate4(self, root, low, high):
        if root == None:
            return True
        if (low != None and root.val <= low) or (high != None and root.val >= high):
            return False
        return self.validate4(root.left, low, root.val) and self.validate4(root.right, root.val, high)





tree1 = TreeNode(1,
             TreeNode(2, TreeNode(4), TreeNode(5)),
             TreeNode(3, TreeNode(6), TreeNode(7))
             )
tree2 = TreeNode(4,
             TreeNode(2, TreeNode(1), TreeNode(3)),
             TreeNode(6, TreeNode(5), TreeNode(7))
             )
result = BST()
result.isValidBST(tree1)
result.isValidBST2(tree1)
result.isValidBST(tree2)
result.isValidBST2(tree2)
result.isValidBST3(tree1)
result.isValidBST3(tree2)


class FBT(object):
    def isValidFST(self, root):
        depth, nodes = self.valid(root)
        return nodes == 2**depth-1

    def valid(self, root):
        if root == None:
            return 0, 0
        left_depth, left_nodes = self.valid(root.left)
        right_depth, right_nodes = self.valid(root.right)
        depth = max(left_depth, right_depth) + 1
        nodes = left_nodes + right_nodes + 1
        return depth, nodes

tree1 = TreeNode(1,
             TreeNode(2, TreeNode(4), TreeNode(5)),
             TreeNode(3, TreeNode(6), TreeNode(7))
             )
tree2 = TreeNode(4,
             TreeNode(2, None, TreeNode(3)),
             TreeNode(6, TreeNode(5), TreeNode(7))
             )
result2 = FBT()
result2.isValidFST(tree1)
result2.isValidFST(tree2)

class CBT(object):
    def isValidCBT(self, root):
        leaf = False
        q = Queue()
        q.put(root)
        while not q.empty():
            cur = q.get()
            if leaf and (cur.left or cur.right):
                return False
            if cur.left:
                q.put(cur.left)
            if not cur.left and cur.right:
                return False
            if cur.right:
                q.put(cur.right)
            if not cur.left or not cur.right:
                leaf = True
        return True

tree1 = TreeNode(1,
             TreeNode(2, TreeNode(4), TreeNode(5)),
             TreeNode(3, TreeNode(6), TreeNode(7))
             )
tree2 = TreeNode(1,
             TreeNode(2, TreeNode(4), None),
             TreeNode(3, TreeNode(6), TreeNode(7))
             )

result3 = CBT()
result3.isValidCBT(tree1)
result3.isValidCBT(tree2)

class balancedBT(object):
    def isValidBalance(self, root):
        depth, balanced =  self.isValid(root)
        return balanced

    def isValid(self, root):
        if root == None:
            return 0, True

        left_depth, left_valid = self.isValid(root.left)
        right_depth, right_valid = self.isValid(root.right)

        if abs(left_depth - right_depth) >= 2:
            return max(left_depth, right_depth) + 1, False

        return max(left_depth, right_depth) + 1, True


tree1 = TreeNode(1,
             TreeNode(2, TreeNode(4), TreeNode(5)),
             TreeNode(3, TreeNode(6), TreeNode(7))
             )

tree2 = TreeNode(1,
             TreeNode(2, TreeNode(3, TreeNode(4), None), None),
             TreeNode(3, None, None))

result4 = balancedBT()
result4.isValidBalance(tree1)
result4.isValidBalance(tree2)









