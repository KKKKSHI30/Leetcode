# Depth-First Search Approach
# Time: O(n)
# Space: O(n)
# 2023.06.27: no
# notes: 这道题考察的重点是哪些方法可以序列化和反序列化，只有DFS的先序遍历，后序遍历，BFS可以
# 中序遍历不可以，因为root节点并不是唯一的，其他三个方法必须要加Null才可以唯一
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    # Serialization
    def serialize(self, root):
        """ Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """

        def rserialize(root, string):
            """ a recursive helper function for the serialize() function."""
            # check base case
            if root is None:
                string += 'None,'
            else:
                string += str(root.val) + ','
                string = rserialize(root.left, string)
                string = rserialize(root.right, string)
            return string

        return rserialize(root, '')

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """

        def rdeserialize(l):
            """ a recursive helper function for deserialization."""
            if l[0] == 'None':
                l.pop(0)
                return None

            root = TreeNode(l[0])
            l.pop(0)
            root.left = rdeserialize(l)
            root.right = rdeserialize(l)
            return root

        data_list = data.split(',')
        root = rdeserialize(data_list)
        return root

# Tests:
root = TreeNode(1)
ser = Codec()
deser = Codec()
ans = deser.deserialize(ser.serialize(root))