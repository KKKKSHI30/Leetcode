# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Iterative Approach (best approach):
# Time: O(m+n)
# Space: O(n)
# 2023.06.17: yes
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy_head = return_point = ListNode(-1)
        while list1 and list2:
            if list1.val <= list2.val:
                dummy_head.next = list1
                list1 = list1.next
            else:
                dummy_head.next = list2
                list2 = list2.next
            dummy_head = dummy_head.next
        if list1:
            dummy_head.next = list1
        if list2:
            dummy_head.next = list2
        return return_point.next

# Recursion Approach:
# Time: O(m+n)
# Space: O(m+n)
# 2023.06.17: no
class Solution2(object):
    def mergeTwoLists(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next,list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1,list2.next)
            return list2

# Test Cases:
a = ListNode(2)
b = ListNode(1, ListNode(3))
test = Solution2()
c = test.mergeTwoLists(a, b)
d = test.mergeTwoLists([],[])



