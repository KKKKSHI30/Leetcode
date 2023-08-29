# 98. Validate Binary Search Tree
import math
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def solution(t):
    def inorder(root):
        nonlocal tmp
        if not root:
            return True
        if not inorder(root.left):
            return False
        if root.value <= tmp:
            return False
        tmp = root.value
        return inorder(root.right)

    tmp = -math.inf
    return inorder(t)

tree = TreeNode(10, TreeNode(5), TreeNode(15, TreeNode(6), TreeNode(20)))
solution(tree)