# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, next = None):
        self.val = x
        self.next = next






"""
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

class Solution2(object):
    # same as solution1
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        p1, p2 = head, head.next
        while p1 != p2:
            if not p2 or not p2.next:
                return False
            p1 = p1.next
            p2 = p2.next.next
        return True

class Solution3:
    # not a good way, saving
    def hasCycle(self, head: ListNode) -> bool:
        nodes_seen = set()
        while head is not None:
            if head in nodes_seen:
                return True
            nodes_seen.add(head)
            head = head.next
        return False

a = ListNode(3, ListNode(1))
b = ListNode(2, a)
# a.next.next = b
test2 = Solution2()
test2.hasCycle(a)
"""
