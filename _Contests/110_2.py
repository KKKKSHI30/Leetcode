# Definition for singly-linked list.
import math
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head == None or head.next == None:
            return head
        fp = head.next
        sp = head
        while fp:
            new_value = self.gcd(fp.val, sp.val)
            sp.next = ListNode(new_value, fp)
            fp, sp = fp.next, sp.next.next
        return head

    def gcd(self, a, b):
        if (b == 0):
            return a
        else:
            return self.gcd(b, a % b)

# Tests:
test = Solution()
test.insertGreatestCommonDivisors(None)
results = test.insertGreatestCommonDivisors(ListNode(7))
results2 = test.insertGreatestCommonDivisors(ListNode(18, ListNode(6, ListNode(10, ListNode(3)))))


