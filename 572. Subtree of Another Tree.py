class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Depth First Search Approach
# Time: O(mn)
# Space: O(m+n)
# 2023.06.29: yes
class Solution:
    def isSubtree(self, root, subRoot):
        def dfs(node):
            if node is None:
                return False
            elif is_identical(node, subRoot):
                return True
            return dfs(node.left) or dfs(node.right)

        def is_identical(node1, node2):
            if node1 is None or node2 is None:
                return node1 is None and node2 is None
            return (node1.val == node2.val and
                    is_identical(node1.left, node2.left) and
                    is_identical(node1.right, node2.right))
        return dfs(root)

# String Matching Approach (KMP)
# Time: O(mn)
# Space: O(m+n)
# 2023.06.29: no
class Solution2:
    def isSubtree(self, root, subRoot):

        # Function to serialize Tree
        def serialize(node, tree_str):
            if node is None:
                tree_str.append('#')
                return

            tree_str.append("^")
            tree_str.append(str(node.val))
            serialize(node.left, tree_str)
            serialize(node.right, tree_str)

        # Knuth-Morris-Pratt algorithm to check if `needle` is in `haystack`
        def kmp(needle, haystack):
            m = len(needle)
            n = len(haystack)

            if n < m:
                return False

            # longest proper prefix which is also suffix
            lps = [0] * m
            # Length of Longest Border for prefix before it.
            prev = 0
            # Iterating from index-1. lps[0] will always be 0
            i = 1

            while i < m:
                if needle[i] == needle[prev]:
                    # Length of Longest Border Increased
                    prev += 1
                    lps[i] = prev
                    i += 1
                else:
                    # Only empty border exist
                    if prev == 0:
                        lps[i] = 0
                        i += 1
                    # Try finding longest border for this i with reduced prev
                    else:
                        prev = lps[prev - 1]

            # Pointer for haystack
            haystack_pointer = 0
            # Pointer for needle.
            # Also indicates number of characters matched in current window.
            needle_pointer = 0

            while haystack_pointer < n:
                if haystack[haystack_pointer] == needle[needle_pointer]:
                    # Matched Increment Both
                    needle_pointer += 1
                    haystack_pointer += 1
                    # All characters matched
                    if needle_pointer == m:
                        return True
                else:
                    if needle_pointer == 0:
                        # Zero Matched
                        haystack_pointer += 1
                    else:
                        # Optimally shift left needle_pointer.
                        # Don't change haystack_pointer
                        needle_pointer = lps[needle_pointer - 1]

            return False

        # Serialize given Nodes
        root_list = []
        serialize(root, root_list)
        r = "".join(root_list)

        subroot_list = []
        serialize(subRoot, subroot_list)
        s = "".join(subroot_list)

        # Check if s is in r
        return kmp(s, r)


# Tree Hash Approach (best approach)
# Time: O(mn)
# Space: O(m+n)
# 2023.06.29: no
class Solution3:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:

        MOD_1 = 1_000_000_007
        MOD_2 = 2_147_483_647

        def hash_subtree_at_node(node, need_to_add):
            if node is None:
                return (3, 7)

            left = hash_subtree_at_node(node.left, need_to_add)
            right = hash_subtree_at_node(node.right, need_to_add)

            left_1 = (left[0] << 5) % MOD_1
            right_1 = (right[0] << 1) % MOD_1
            left_2 = (left[1] << 7) % MOD_2
            right_2 = (right[1] << 1) % MOD_2

            hashpair = ((left_1 + right_1 + node.val) % MOD_1,
                        (left_2 + right_2 + node.val) % MOD_2)

            if need_to_add:
                memo.add(hashpair)

            return hashpair

        # List to store hashed value of each node.
        memo = set()

        # Calling and adding hash to List
        hash_subtree_at_node(root, True)

        # Storing hashed value of subRoot for comparison
        s = hash_subtree_at_node(subRoot, False)

        # Check if hash of subRoot is present in memo
        return s in memo

# Tests:
a = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
b = TreeNode(4, TreeNode(1), TreeNode(2))
c = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0))), TreeNode(5))
d = TreeNode(4, TreeNode(1), TreeNode(2))
e = TreeNode(3, TreeNode(4, TreeNode(1)), TreeNode(5, TreeNode(2)))
f = TreeNode(3, TreeNode(1), TreeNode(2))
test = Solution3()
result = test.isSubtree(a,b)
result2 = test.isSubtree(c,d)
result3 = test.isSubtree(e,f)
