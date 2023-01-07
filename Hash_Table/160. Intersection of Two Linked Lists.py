class ListNode(object):
    def __init__(self, x, next = None):
        self.val = x
        self.next = next


class Solution:
    # hash table method, which is what I thought first
    def getIntersectionNode(self, headA, headB):
        nodes_in_B = set()

        while headB is not None:
            nodes_in_B.add(headB)
            headB = headB.next

        while headA is not None:
            # if we find the node pointed to by headA,
            # in our set containing nodes of B, then return the node
            if headA in nodes_in_B:
                return headA
            headA = headA.next
        return None


class Solution2:
    # important method
    def getIntersectionNode(self, headA, headB):
        p1 = headA
        p2 = headB
        while p1 != p2:
            if p1:
                p1 = p1.next
            else:
                p1 = headB
            if p2:
                p2 = p2.next
            else:
                p2 = headA
        return p1


a = ListNode(2, ListNode(6, ListNode(4)))
b = ListNode(1, ListNode(5))
test = Solution2()
test.getIntersectionNode(a, b)
