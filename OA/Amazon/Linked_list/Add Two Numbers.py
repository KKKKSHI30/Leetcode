# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        rvalue = ListNode()
        head = rvalue
        addon = False
        check = False
        while l1 or l2 or addon:
            if check:
                rvalue.next = ListNode()
                rvalue = rvalue.next
            if l1 and l2:
                sum = l1.val + l2.val
                if addon:
                    if sum >= 9:
                        addon = True
                        rvalue.val = sum - 10 + 1
                    else:
                        addon = False
                        rvalue.val = sum + 1
                else:
                    if sum > 9:
                        addon = True
                        rvalue.val = sum -10
                    else:
                        addon = False
                        rvalue.val = sum
                l1 = l1.next
                l2 = l2.next
            elif l1:
                if addon:
                    if l1.val == 9:
                        addon = True
                        rvalue.val  = l1.val - 10 + 1
                    else:
                        addon = False
                        rvalue.val = l1.val + 1
                else:
                    addon = False
                    rvalue.val = l1.val
                l1 = l1.next
            elif l2:
                if addon:
                    if l2.val == 9:
                        addon = True
                        rvalue.val  = l2.val - 10 + 1
                    else:
                        addon = False
                        rvalue.val = l2.val + 1
                else:
                    addon = False
                    rvalue.val = l2.val
                l2 = l2.next
            else:
                rvalue.val = 1
                addon = False
            check = True
        return head


class Solution2(object):
    # time saving
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        result = 0
        carry = 0
        dummyHead = ListNode(0)
        temp = dummyHead

        while l1 or l2 or carry:
            if l1 != None and l2 != None:
                result = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            elif l1 == None and l2 == None:
                result = carry
            elif l1 == None:
                result = l2.val + carry
                l2 = l2.next
            elif l2 == None:
                result = l1.val + carry
                l1 = l1.next

            if result > 9:
                carry = 1
                result -= 10
            else:
                carry = 0
            temp.next = ListNode(result)
            temp = temp.next

        return dummyHead.next


class Solution3(object):
    # space saving
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        dummyHead = ListNode(0)
        l3 = dummyHead
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            columnSum = l1_val + l2_val + carry
            carry = columnSum // 10

            newNode = ListNode(columnSum % 10)
            l3.next = newNode
            l3 = l3.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummyHead.next

test = Solution()
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
l3 = ListNode(0)
l4 = ListNode(0)
l5 = ListNode(9, ListNode(9, ListNode(9)))
l6 = ListNode(9)
l7 = ListNode(4)
l8 = ListNode(5)
r1 = test.addTwoNumbers(l1, l2)
r2 = test.addTwoNumbers(l3, l4)
r3 = test.addTwoNumbers(l5, l6)
r4 = test.addTwoNumbers(l7,l8)
