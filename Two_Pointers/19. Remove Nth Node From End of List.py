# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p1 = head
        p2 = head
        for i in range(n):
            p1 = p1.next
        if p1:
            return head.next
        while p1.next:
            p2 = p2.next
            p1 = p1.next
        p2.next = p2.next.next
        return head

