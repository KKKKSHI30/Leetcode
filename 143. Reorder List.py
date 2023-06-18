# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

# Reverse the Second Part of the List and Merge Two Sorted Lists Approach
# Time: O(n)
# Space: O(1)
# Notes: 切半，然后后半部分reverse，再拼起来
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        fp = sp = head
        while fp and fp.next:
            fp = fp.next.next
            sp = sp.next
        prev, cur = None, sp
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        # curr.next, prev, curr = prev, curr, curr.next (smart)
        p1, p2 = head, prev
        while p2.next:
            p1.next, p1 = p2, p1.next
            p2.next, p2 = p1, p2.next

# Test
a = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
test = Solution()
test.reorderList(a)

