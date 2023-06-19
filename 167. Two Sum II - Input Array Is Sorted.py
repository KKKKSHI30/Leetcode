# Two Pointers Approach (best approach)
# Time: O(n)
# Space: O(1)
# 2023.06.18: no
# notes: 滑动窗口不一定起始点一样，可以一个从右一个从左，因为是按从小到大顺序排列
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        lp, rp = 0, len(numbers)-1
        while lp < rp:
            if numbers[lp] + numbers[rp] == target:
                return [lp+1, rp+1]
            elif numbers[lp] + numbers[rp] > target:
                rp -= 1
            else:
                lp += 1

# Tests
test = Solution()
test.twoSum([2,7,11,15], 9)

