class Solution:
    # brute force methods, same as me
    def maxArea(self, height):
        maxarea = 0
        for left in range(len(height)):
            for right in range(left + 1, len(height)):
                width = right - left
                maxarea = max(maxarea, min(height[left], height[right]) * width)
        return maxarea


class Solution2:
    # double pointer
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
test2 = Solution2()
test2.maxArea([1,8,6,2,5,4,8,3,7])