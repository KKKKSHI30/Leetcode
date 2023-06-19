# Two Pointers Approach
# Time: O(n)
# Space: O(1)
# 2023.06.18: yes
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        sp = fp = 0
        while fp < len(nums):
            if nums[fp] == val:
                fp += 1
            else:
                nums[sp] = nums[fp]
                sp += 1
                fp += 1
        return sp

# Two Pointers - when elements to remove are rare
# Time: O(n)
# Space: O(1)
# 2023.06.18: no
# notes: 本质是将一样的element和最后的交换，用来减少element的移动，但是time和space complexity是一样的
# 快不了太多
class Solution2(object):
    def removeElement(self, nums, val):
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]
                # Reduce array size by one
                n -= 1
            else:
                i += 1
        return n

a = [1,2,3,4,2,1,1,3,2]
test = Solution2()
result = test.removeElement(a, 2)
