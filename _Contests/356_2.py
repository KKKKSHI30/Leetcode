# Sliding Winow
# Time: O(n^2)
# Space: O(1)
# 2023.07.29: no
# notes: 从第零个数字开始遍历，看有几种可能达成，然后从第一个数字开始，以此类推
class Solution:
    def countCompleteSubarrays(self, nums):
        n = len(nums)
        le = len(set(nums))
        ans = 0
        for i in range(n):
            s = set()
            for j in range(i,n):
                s.add(nums[j])
                if len(s) == le:
                    ans += n - j
                    break
        return ans

# Tests:
test = Solution()
test.countCompleteSubarrays([1,3,1,2,2])
test.countCompleteSubarrays(nums = [5,5,5,5])

