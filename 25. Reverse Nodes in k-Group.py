# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Recursive Approach:
# Time: O(n)
# Space: O(n/k)
# 2023.06.19: no
# notes: 非常精妙，这个是206->92->25这样的顺序，notes偏多，细节我记录在下面
class Solution:
    # 这只是个普通的recursion来翻转linkedlist的方法，最后返回新的头结点（原尾节点）即可
    def reverseLinkedList(self, head, k):

        # Reverse k nodes of the given linked list.
        # This function assumes that the list contains
        # atleast k nodes.
        new_head, ptr = None, head
        while k:
            # Keep track of the next node to process in the
            # original list
            next_node = ptr.next

            # Insert the node pointed to by "ptr"
            # at the beginning of the reversed list
            ptr.next = new_head
            new_head = ptr

            # Move on to the next node
            ptr = next_node

            # Decrement the count of nodes to be reversed by 1
            k -= 1

        # Return the head of the reversed list
        return new_head

    def reverseKGroup(self, head, k):

        count = 0 # 计数
        ptr = head

        # First, see if there are atleast k nodes
        # left in the linked list.
        while count < k and ptr:
            ptr = ptr.next
            count += 1

        # If we have k nodes, then we reverse them
        if count == k:
            # Reverse the first k nodes of the list and
            # get the reversed list's head.
            # 单纯翻转小linked lists
            reversedHead = self.reverseLinkedList(head, k)

            # Now recurse on the remaining linked list. Since
            # our recursion returns the head of the overall processed
            # list, we use that and the "original" head of the "k" nodes
            # to re-wire the connections.
            # 把尾结点（就是老的头结点）的下一个接到翻转过的尾结点，重点！非常经典一句话
            head.next = self.reverseKGroup(ptr, k)
            return reversedHead
        # 写的其实很不清晰， 本来的意思就是，如果count不够到k个字符，就返回不到k个nodes的头结点，也就是什么都不需要翻转
        return head

# Recursive Approach:
# Time: O(n)
# Space: O(n/k)
# 2023.06.19: no
# notes: labuladong的方法，比标答更好，很容易理解
# 核心思想是把终止条件改一下，以前是到None为止停止翻转，现在是到next node不需要翻转的时候停，很巧妙
class Solution3(object):
    # 反转区间 [a, b) 的元素，注意是左闭右开,重点
    def reverse(self, a, b):
        pre, cur, nxt = None, a, a
        # while  终止的条件改一下就行了
        while cur != b:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        # 返回反转后的头结点
        return pre

    def reverseKGroup(self, head, k):
        if not head:
            return None
        # 区间 [a, b) 包含 k 个待反转元素
        a, b = head, head
        for i in range(k):
            # 不足 k 个，不需要反转，base case
            if not b:
                return head
            b = b.next
        # 反转前 k 个元素, 翻转到b
        new_head = self.reverse(a, b)
        # 递归反转后续链表并连接起来
        a.next = self.reverseKGroup(b, k)
        return new_head


# Iterative O(1) space Approach:
# Time: O(n)
# Space: O(1)
# 2023.06.18: no
class Solution2:

    def reverseLinkedList(self, head, k):

        # Reverse k nodes of the given linked list.
        # This function assumes that the list contains
        # atleast k nodes.
        new_head, ptr = None, head
        while k:
            # Keep track of the next node to process in the
            # original list
            next_node = ptr.next

            # Insert the node pointed to by "ptr"
            # at the beginning of the reversed list
            ptr.next = new_head
            new_head = ptr

            # Move on to the next node
            ptr = next_node

            # Decrement the count of nodes to be reversed by 1
            k -= 1

        # Return the head of the reversed list
        return new_head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        ptr = head
        ktail = None

        # Head of the final, moified linked list
        new_head = None

        # Keep going until there are nodes in the list
        while ptr:
            count = 0

            # Start counting nodes from the head
            ptr = head

            # Find the head of the next k nodes
            while count < k and ptr:
                ptr = ptr.next
                count += 1

            # If we counted k nodes, reverse them
            if count == k:

                # Reverse k nodes and get the new head
                revHead = self.reverseLinkedList(head, k)

                # new_head is the head of the final linked list
                # 这个是当没有头的时候，也就是第一次reverse的时候的尾巴，之后的情况，new_head都有值，不会再进这个if statement
                if not new_head:
                    new_head = revHead

                # ktail is the tail of the previous block of
                # reversed k nodes
                # 第一次赋值才会跳过，因为第一个reverse的前面是None，之后都会进，除非最后一段，根本连前面的if都没进
                if ktail:
                    ktail.next = revHead

                ktail = head
                head = ptr

        # attach the final, possibly un-reversed portion
        # 不需要翻转的时候，他的next就会进这个，因为head永远是头，revhead永远是尾或者新头
        if ktail:
            ktail.next = head

        return new_head if new_head else head


# Tests:
a = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
test = Solution2()
test.reverseKGroup(a, 2)

