# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    # 可以优化掉空间，直接用计数有没有到k个就可以了
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return None
        saving_lst = []
        cur = head
        temp_cur = head
        count = 1
        max = k
        last_end = None
        if k == 1:
            return head
        while cur or len(saving_lst) == k:
            if len(saving_lst) == k:
                for i in range(k):
                    temp_cur_next = temp_cur.next
                    # if temp cur is head
                    if i == 0:
                        if last_end:
                            last_end.next = saving_lst[-1]
                        last_end = temp_cur
                        temp_cur.next = cur
                        temp_cur = temp_cur_next
                    else:
                        temp_cur.next = saving_lst[i-1]
                        temp_cur = temp_cur_next
                # situation that len(saving_lst) == k and cur == None
                if not cur:
                    break
                # reset for next loop
                saving_lst = []
                temp_cur = cur
                saving_lst.append(cur)
            else:
                saving_lst.append(cur)
            if count < max:
                count += 1
                head = head.next
            cur = cur.next
        return head


node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
test = Solution()
result = test.reverseKGroup(node, 3)
node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
result2 = test.reverseKGroup(node, 2)
node2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
result3 = test.reverseKGroup(node2, 2)


class Solution2:
    # get the head and new_head(old end), using recursion to link

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

        count = 0
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
            reversedHead = self.reverseLinkedList(head, k)

            # Now recurse on the remaining linked list. Since
            # our recursion returns the head of the overall processed
            # list, we use that and the "original" head of the "k" nodes
            # to re-wire the connections.
            head.next = self.reverseKGroup(ptr, k)
            return reversedHead
        return head


class Solution3:
    # same thought as me, but more convient and optimized
    # Space: O(1) Time: O(n)
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
                if not new_head:
                    new_head = revHead

                # ktail is the tail of the previous block of
                # reversed k nodes
                if ktail:
                    ktail.next = revHead

                ktail = head
                head = ptr

        # attach the final, possibly un-reversed portion
        if ktail:
            ktail.next = head

        return new_head if new_head else head