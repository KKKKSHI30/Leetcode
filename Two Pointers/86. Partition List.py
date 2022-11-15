# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummy_head = ListNode(-1)
        cur = dummy_head
        dummy_head2 = ListNode(-1)
        cur2 = dummy_head2
        while head:
            if head.val < x:
                cur.next = head
                head = head.next
                cur = cur.next
            else:
                cur2.next = head
                head = head.next
                cur2 = cur2.next
        cur2.next = None
        cur.next = dummy_head2.next
        return dummy_head.next


a = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
test = Solution()
b = test.partition(a, 3)
c = test.partition([], 3)

