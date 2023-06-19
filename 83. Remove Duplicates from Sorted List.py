# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Straight-Forward Approach
# Time: O(n)
# Space: O(1)
# 2023.06.18: yes
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        sp = fp = head
        while fp:
            if sp.val == fp.val:
                fp = fp.next
            else:
                sp.next = fp
                fp = fp.next
                sp = sp.next
        if sp:
            sp.next = None
        return head

# Tests:
a = ListNode(1, ListNode(1, ListNode(2, ListNode(2, ListNode(3, ListNode(3))))))
test = Solution()
b = test.deleteDuplicates(a)
c = test.deleteDuplicates(None)
