# Approach (best approach)
# Time: O(n)
# Space: O(1)
# 2023.06.18: yes

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        fp, sp = 0, 0
        while fp < len(nums):
            if nums[fp] == 0:
                fp += 1
            else:
                nums[sp] = nums[fp]
                sp += 1
                fp += 1
        for i in range(sp, len(nums)):
            nums[i] = 0
        return nums

# Approach (best approach)
# Time: O(n)
# Space: O(1)
# 2023.06.18: yes
# notes: mark the place we don't have non zero
class Solution2(object):
    def moveZeroes(self,nums):
        lastNonZeroFoundAt = 0
        for cur in range(len(nums)):
            if nums[cur] != 0:
                nums[lastNonZeroFoundAt], nums[cur] = nums[cur], nums[lastNonZeroFoundAt]
                lastNonZeroFoundAt += 1

test = Solution()
a = test.moveZeroes([1,2,0,3,2,0])
b = test.moveZeroes([0,0,1])
c = test.moveZeroes([0])