# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Two Pointers Approach (best approach):
# Time: O(n)
# Space: O(1)
# 2023.06.17: yes
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummy_small = cur_small = ListNode(-1)
        dummy_large = cur_large = ListNode(-1)
        while head:
            if head.val >= x:
                cur_large.next = ListNode(head.val)
                cur_large = cur_large.next
            else:
                cur_small.next = ListNode(head.val)
                cur_small = cur_small.next
            head = head.next
        cur_small.next = dummy_large.next
        return dummy_small.next


a = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
test = Solution()
b = test.partition(a, 3)
c = test.partition([], 3)

