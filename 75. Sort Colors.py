# One Pass Algorithm (best approach)
# Time: O(n)
# Space: O(1)
# 2023.06.24: yes
# notes: 就是荷兰国旗问题，一个头，一个尾
class Solution:
    def sortColors(self, nums):
        """
        Dutch National Flag problem solution.
        """
        # for all idx < p0 : nums[idx < p0] = 0
        # curr is an index of element under consideration
        p0 = curr = 0
        # for all idx > p2 : nums[idx > p2] = 2
        p2 = len(nums) - 1

        while curr <= p2:
            if nums[curr] == 0:
                nums[p0], nums[curr] = nums[curr], nums[p0]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:
                curr += 1

# Tests:
nums = [2,0,2,1,1,0]
nums2 = [2,0,1]
nums3 = [1,1,0,0,2,2]
test = Solution()
test.sortColors(nums)
test.sortColors(nums2)
test.sortColors(nums3)






