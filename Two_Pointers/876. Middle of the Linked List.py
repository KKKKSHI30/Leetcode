# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p1, p2 = head, head
        if not p1:
            return p2
        while p1 and p1.next:
            p1 = p1.next.next
            p2 = p2.next
        return p2