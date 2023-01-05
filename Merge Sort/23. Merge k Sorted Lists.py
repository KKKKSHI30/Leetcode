import heapq
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    # Optimize Approach 2 by Priority Queue
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # Since python3 will have some comparison bugs, I have to add these two lines for heapq comparison
        ListNode.__eq__ = lambda self, other: self.val == other.val
        ListNode.__lt__ = lambda self, other: self.val < other.val

        dummy_head = ListNode(-1)  # create a dummy head
        cur = dummy_head
        h = []  # create the heapq
        for i in lists:
            # check for the list is an empty list or not
            if i:
                heapq.heappush(h, (i.val, i))
            # when the heapq still have some element in it, continue the loop
        while h:
            val, node = heapq.heappop(h)
            cur.next = node
            node = node.next
            cur = cur.next
            # check if the node reaches the end, and whether to put the new element in the heapq
            if node:
                heapq.heappush(h, (node.val, node))
            # return the results
        return dummy_head.next


class Solution2(object):
    # Merge with Divide And Conquer
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else None

    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
        if not l1:
            point.next=l2
        else:
            point.next=l1
        return head.next



a = ListNode(1, ListNode(4, ListNode(5)))
b = ListNode(1, ListNode(3, ListNode(4)))
c = ListNode(2, ListNode(6))
test = Solution()
d = test.mergeKLists([a,b,c])


class Solution3(object):
    # brute force, not recommended
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        self.nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next
        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next
