# A String Representation Approach
# Time: O(n^2)
# Space: O(n^2)
# 2023.06.27: no
# notes: 序列化一个树，然后看这个树的序列化在不在里面
import collections
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findDuplicateSubtrees(self, root):
        def traverse(node):
            if not node:
                return ""
            representation = ("(" + traverse(node.left) + ")" + str(node.val)
                              + "(" + traverse(node.right) + ")")
            cnt[representation] += 1
            if cnt[representation] == 2:
                res.append(node)
            return representation
        cnt = collections.defaultdict(int)
        res = []
        traverse(root)
        return res


# An Optimized Approach
# Time: O(n)
# Space: O(n)
# 2023.06.27: no
# notes: 用triplet来表示一个树，如果出现过这个点，就记录并给一个id，下次再出现就可以直接调用这个id，并且一个id数字就记录了一种树
class Solution2:
    def findDuplicateSubtrees(self, root):
        def traverse(node):
            if not node:
                return 0
            triplet = (traverse(node.left), node.val, traverse(node.right))
            if triplet not in triplet_to_id:
                triplet_to_id[triplet] = len(triplet_to_id) + 1
            id = triplet_to_id[triplet]
            cnt[id] += 1
            if cnt[id] == 2:
                res.append(node)
            return id
        triplet_to_id = dict()
        cnt = collections.defaultdict(int)
        res = []
        traverse(root)
        return res

# Tests:
t = TreeNode(1)
t.left = TreeNode(2)
t.left.left = TreeNode(4)
t.right = TreeNode(3)
t.right.left = TreeNode(2)
t.right.left.left = TreeNode(4)
t.right.right = TreeNode(4)
test = Solution2()
test.findDuplicateSubtrees(t)