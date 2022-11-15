# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy_head = ListNode(-1)
        cur = dummy_head
        while list1 and list2:
            if list1.val >= list2.val:
                cur.next = list2
                cur = cur.next
                list2 = list2.next
            else:
                cur.next = list1
                cur = cur.next
                list1 = list1.next
        if list1:
            cur.next = list1
        if list2:
            cur.next = list2
        return dummy_head.next

a = ListNode(1, ListNode(2, ListNode(4)))
b = ListNode(1, ListNode(3, ListNode(4)))

test = Solution()
c = test.mergeTwoLists(a, b)
d = test.mergeTwoLists([],[])



