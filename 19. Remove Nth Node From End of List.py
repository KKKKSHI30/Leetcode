# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# One Pass Algorithm Approach (best approach):
# Time: O(l), l is the length of nodes
# Space: O(1)
# 2023.06.17: yes

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy_head = ListNode(-1)
        dummy_head.next = head
        fp = sp = dummy_head
        for i in range(n):
            fp = fp.next
        while fp.next:
            fp = fp.next
            sp = sp.next
        sp.next = sp.next.next
        return dummy_head.next

# Two Pass Algorithm Approach:
# Time: O(l), l is the length of nodes
# Space: O(1)
# 2023.06.17: yes
class Solution2(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        length = 0
        first = head
        while first is not None:
            length += 1
            first = first.next
        length -= n
        first = dummy
        while length > 0:
            length -= 1
            first = first.next
        first.next = first.next.next
        return dummy.next

# Tests
a = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
b = ListNode(1)
c= ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
test = Solution()
result = test.removeNthFromEnd(a, 2)
result2 = test.removeNthFromEnd(b, 1)
result3 = test.removeNthFromEnd(c, 4)


