# Fisher-Yates Algorithm
# Time: O(n)
# Space: O(n)
# 2023.08.04: no
# notes: Reservoir Sampling，水塘抽样法，很玄学，证明更玄学，先跳过
import random
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self):
        r = random.Random()
        i = 0
        res = 0
        p = self.head
        # while 循环遍历链表
        while p != None:
            i = i + 1
            # 生成一个 [0, i) 之间的整数
            # 这个整数等于 0 的概率就是 1/i
            if 0 == r.randint(0, i - 1):
                res = p.val
            p = p.next
        return res

    # 标答
    def getRandom2(self):
        """
        Returns a random node's value.
        """
        scope = 1
        chosen_value = 0
        curr = self.head

        while curr:
            # decide whether to include the element in reservoir
            if random.random() < 1 / scope:
                chosen_value = curr.val
            # move on to the next node
            curr = curr.next
            scope += 1
        return chosen_value
# Tests:
obj = Solution(ListNode(1, ListNode(2, ListNode(3))))
param_1 = obj.getRandom()