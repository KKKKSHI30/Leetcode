# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Copy into Array List and then Use Two Pointer Technique
# Time: O(n)
# Space: O(n)
# 2023.06.19: yes
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        cur = head
        arr = []
        while cur:
            arr.append(cur.val)
            cur = cur.next
        begin_pointer, end_pointer = 0, len(arr)-1
        while begin_pointer <= end_pointer:
            if arr[begin_pointer] == arr[end_pointer]:
                begin_pointer += 1
                end_pointer -= 1
            else:
                return False
        return True

# Reverse Second Half In-place(best approach)
# Time: O(n)
# Space: O(1)
# 2023.06.19: yes
class Solution2(object):
    def reverse(self, head):
        prev = None
        cur = head
        while cur:
            next_temp = cur.next
            cur.next = prev
            prev = cur
            cur = next_temp
        return prev

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fp = sp = head
        while fp and fp.next:
            sp = sp.next
            fp = fp.next.next
        rev_head = self.reverse(sp)
        cur = head
        while rev_head:
            if rev_head.val == cur.val:
                rev_head = rev_head.next
                cur = cur.next
            else:
                return False
        return True

# Recursive Approach(advanced)
# Time: O(n)
# Space: O(n)
# 2023.06.19: no
# notes: 运用了linked list的后序遍历，主要是太优美了写的，令人折服
class Solution3(object):
    left = None

    def isPalindrome(self, head):
        global left
        left = head
        return self.traverse(head)

    def traverse(self, right):
        global left
        if right is None:
            return True
        res = self.traverse(right.next)
        # 后序遍历代码， 打印的时候就是倒着打印
        res = res and (right.val == left.val)  # 递归一定要去递归结果
        left = left.next # 常规的left是正着打印，正好比对正倒序一不一样
        return res



# Tests:
a = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
b = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
test = Solution3()
test.isPalindrome(a)
test.isPalindrome(b)
