# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        fast, slow = head, head
        while fast:
            if fast.val == slow.val:
                fast = fast.next
            else:
                slow.next = fast
                slow = slow.next
                fast = fast.next
        slow.next = None
        return head


a = ListNode(1, ListNode(1, ListNode(2, ListNode(2, ListNode(3, ListNode(3))))))
test = Solution()
b = test.deleteDuplicates(a)
c = test.deleteDuplicates(None)
