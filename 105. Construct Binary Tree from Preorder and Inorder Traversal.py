# Recursion Approach:
# Time: O(n)
# Space: O(n)
# 2023.06.27: no
# notes: 这道题就是654的加难版，本质上是一样的，找到root节点是什么，然后分成左边和右边去递归完成
# 其中val的值是不重复的，还可以用hash表来快速查找

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        valToIndex = {}
        for i in range(len(inorder)):
            valToIndex[inorder[i]] = i

        def build(preorder, preStart, preEnd, inorder, inStart, inEnd):
            if preStart > preEnd:
                return None

            # root 节点对应的值就是前序遍历数组的第一个元素
            rootVal = preorder[preStart]
            # rootVal 在中序遍历数组中的索引
            index = valToIndex.get(rootVal)

            leftSize = index - inStart

            # 先构造出当前根节点
            root = TreeNode(rootVal)

            # 递归构造左右子树
            root.left = build(preorder, preStart + 1, preStart + leftSize,
                              inorder, inStart, index - 1)

            root.right = build(preorder, preStart + leftSize + 1, preEnd,
                               inorder, index + 1, inEnd)
            return root
        return build(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)

# Recursion Approach:
# Time: O(n)
# Space: O(n)
# 2023.06.27: no
# notes: 官方答案，非常简洁而且不用算数字，很方便
class Solution2:
    def buildTree(self, preorder, inorder):

        def array_to_tree(left, right):
            nonlocal preorder_index
            # if there are no elements to construct the tree
            if left > right: return None

            # select the preorder_index element as the root and increment it
            root_value = preorder[preorder_index]
            root = TreeNode(root_value)


            preorder_index += 1

            # build left and right subtree
            # excluding inorder_index_map[root_value] element because it's the root
            root.left = array_to_tree(left, inorder_index_map[root_value] - 1)
            root.right = array_to_tree(inorder_index_map[root_value] + 1, right)

            return root

        preorder_index = 0

        # build a hashmap to store value -> its index relations
        inorder_index_map = {}
        for index, value in enumerate(inorder):
            inorder_index_map[value] = index

        return array_to_tree(0, len(preorder) - 1)

# Test:
test = Solution2()
test.buildTree(preorder = [3,9,20,15,7], inorder = [9,3,15,20,7])


