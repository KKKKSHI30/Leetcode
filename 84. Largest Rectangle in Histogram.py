# Using Stack (best approach)
# Time: O(n)
# Space: O(n)
# 2023.07.20: no
# notes: 这道题，非常好，写一下思路， O(n)的情况
# 要保证stack是increasing的order，放stack的时候放index就可以，因为可以直接看到元素
# 如果下一个element比stack前一个元素大，直接压
# 如果下一个element比stack前一个元素小，弹出前一个元素，算一下前一个元素的前一个元素的index是多少，就可以看出，这个前一个元素
# 最大的面积是多少；一直弹出栈中元素，直到下一个元素比前面的元素大，弹完也可以
# 全部遍历完一遍后，stack中的元素一个个弹出的时候，看前一个元素的index，确认面积
class Solution:
    def largestRectangleArea(self, heights):
        stack = [-1]
        max_area = 0
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                current_height = heights[stack.pop()]
                current_width = i - stack[-1] - 1
                max_area = max(max_area, current_height * current_width)
            stack.append(i)

        while stack[-1] != -1:
            current_height = heights[stack.pop()]
            current_width = len(heights) - stack[-1] - 1
            max_area = max(max_area, current_height * current_width)
        return max_area

# Divide and Conquer
# Time: O(nlogn)
# Space: O(n^2)
# 2023.07.20: no
# notes: 利用merge sort的方法去算出最大的面积，由最小的高度进行分割
class Solution2:
    def largestRectangleArea(self, heights):
        def calculateArea(heights, start, end):
            if start > end:
                return 0
            min_index = start
            for i in range(start, end + 1):
                if heights[min_index] > heights[i]:
                    min_index = i
            return max(
                heights[min_index] * (end - start + 1),
                calculateArea(heights, start, min_index - 1),
                calculateArea(heights, min_index + 1, end),
            )
        return calculateArea(heights, 0, len(heights) - 1)

# Tests:
test = Solution2()
test.largestRectangleArea([2,1,5,6,2,3])