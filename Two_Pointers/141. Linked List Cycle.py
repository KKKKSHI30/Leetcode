# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, next = None):
        self.val = x
        self.next = next

class Solution:
    def hasCycle(self, head):
        if not head:
            return False
        p1, p2 = head.next, head
        while p1 != p2:
            if not p1 or not p1.next:
                return False
            p1 = p1.next.next
            p2 = p2.next
        return True

a = ListNode(3, ListNode(1))
b = ListNode(2, a)
# a.next.next = b
test = Solution()
test.hasCycle(a)
