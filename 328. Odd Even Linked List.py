# Two Pointers
# Time: O(mlogm) for sorting
# Space: O(n)
# 2023.07.06: yes
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        i = 0
        odd_head = odd_cur = ListNode(-1)
        even_head = even_cur =  ListNode(-1)
        while head:
            if i % 2 == 0:
                odd_cur.next = head
                odd_cur = odd_cur.next
            else:
                even_cur.next = head
                even_cur = even_cur.next
            i += 1
            head = head.next
        odd_cur.next = even_head.next
        even_cur.next = None
        return odd_head.next

# Tests:
test = Solution()
result2 = test.oddEvenList(ListNode(2, ListNode(1, ListNode(3, ListNode(5, ListNode(6, ListNode(4, ListNode(7))))))))
result = test.oddEvenList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))


