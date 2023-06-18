class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Iterative Approach (best approach):
# Time: O(n)
# Space: O(1)
# 2023.06.17: yes
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev

# Recursive Approach:
# Time: O(n)
# Space: O(n)
# 2023.06.17: no
# notes: 走到最后一个，然后保留前一个，转换方向即可
class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:
        if (not head) or (not head.next):
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p

a = ListNode(1, ListNode(2, ListNode(3)))
test = Solution2()
result = test.reverseList(a)

