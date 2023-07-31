# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        cur = head
        prev = None
        cur_next = cur.next
        cur.next = prev
        while cur:
            prev = cur
            cur = cur_next
            if not cur_next.next:
                cur.next = prev
                return cur
            cur_next = cur_next.next
            cur.next = prev


node = ListNode(1, ListNode(2, ListNode(3)))
test = Solution()
result = test.reverseList(node)


class Solution2:
    # 啊啊！！！！标答了背住！！！！！
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        return prev


class Solution3:
    # recursive solution 但是记住怎么做
    def reverseList(self, head: ListNode) -> ListNode:
        if (not head) or (not head.next):
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p

node = ListNode(1, ListNode(2, ListNode(3)))
test = Solution3()
result = test.reverseList(node)