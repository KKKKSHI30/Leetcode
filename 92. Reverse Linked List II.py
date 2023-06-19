# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Two Recursive Approach:
# Time: O(n)
# Space: O(n)
# 2023.06.18: no
# notes: 很难理解，建议看https://labuladong.github.io/algo/di-yi-zhan-da78c/shou-ba-sh-8f30d/di-gui-mo--10b77/
# 1. 如何用recursion翻转linked list
# 2. 如何用recursion翻转前n的linked list，在最后一步的时候，保存下一个节点是什么就可以了， recursion的话就是接触到base case的情况
# 3. 如何用recursion翻转中间几个内容
class Solution(object):
    successor = None
    # reverse the previous N elements
    def reverseN(self, head, n):
        global successor
        if n == 1:
            successor = head.next
            return head
        last = self.reverseN(head.next, n - 1)
        head.next.next = head
        head.next = successor
        return last

    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if left == 1:
            return self.reverseN(head, right)
        head.next = self.reverseBetween(head.next, left - 1, right - 1)
        return head

# Recursive Approach:
# Time: O(n)
# Space: O(n)
# 2023.06.18: no
# notes: 完全没懂，嗯。。
class Solution2:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return None
        left, right = head, head
        stop = False
        def recurseAndReverse(right, m, n):
            nonlocal left, stop
            if n == 1:
                return
            right = right.next
            if m > 1:
                left = left.next
            recurseAndReverse(right, m - 1, n - 1)
            # In case both the pointers cross each other or become equal, we
            # stop i.e. don't swap data any further. We are done reversing at this
            # point.
            if left == right or right.next == left:
                stop = True
            if not stop:
                left.val, right.val = right.val, left.val
                # Move left one step to the right.
                # The right pointer moves one step back via backtracking.
                left = left.next
        recurseAndReverse(right, m, n)
        return head


# Iterative Link Reversal Approach (best approach):
# Time: O(n)
# Space: O(1)
# 2023.06.18: no
# notes: 重点是把整个Linked list不需要的部分左挪，然后记录下头结点和尾节点，一步步倒过去，记录最后的节点，连接首尾
# iterative 的方法不难
class Solution3:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        # Empty list
        if not head:
            return None

        # Move the two pointers until they reach the proper starting point
        # in the list.
        cur, prev = head, None
        while m > 1:
            prev = cur
            cur = cur.next
            m, n = m - 1, n - 1

        # The two pointers that will fix the final connections.
        tail, con = cur, prev

        # Iteratively reverse the nodes until n becomes 0.
        while n:
            third = cur.next
            cur.next = prev
            prev = cur
            cur = third
            n -= 1

        # Adjust the final connections as explained in the algorithm
        if con:
            con.next = prev
        else:
            head = prev
        tail.next = cur
        return head

# Tests:
a = ListNode(1,ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
test = Solution3()
test.reverseBetween(a,2,4)




