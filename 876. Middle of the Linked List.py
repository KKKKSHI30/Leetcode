# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Fast and Slow Pointer Approach (best approach):
# Time: O(n)
# Space: O(1)
# 2023.06.17: yes
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy_head = fp = sp = ListNode(-1)
        dummy_head.next = head
        while fp:
            if fp.next:
                fp = fp.next.next
                sp = sp.next
            else:
                break
        if not fp:
            return sp
        else:
            return sp.next

# Output to Array Approach:
# Time: O(n)
# Space: O(n)
# 2023.06.17: yes
class Solution2:
    def middleNode(self, head: ListNode) -> ListNode:
        arr = [head]
        while arr[-1].next:
            arr.append(arr[-1].next)
        return arr[len(arr) // 2]

# Test:
a = ListNode(1,ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
b = ListNode(1,ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
test = Solution()
test.middleNode(a)
test.middleNode(b)


