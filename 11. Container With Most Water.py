# Two Pointer Algorithm (best approach)
# Time: O(n)
# Space: O(1)
# 2023.06.24: no
# notes: 这个证明有点玄，但是就是two pointer,指针永远从矮的往高的走，因为往中间走的时候，只有越来越高才会beneficial
class Solution:
    def maxArea(self, height):
        maxarea = 0
        left = 0
        right = len(height) - 1

        while left < right:
            width = right - left
            maxarea = max(maxarea, min(height[left], height[right]) * width)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return maxarea

test = Solution()
test.maxArea([1,8,6,2,5,4,8,3,7])
