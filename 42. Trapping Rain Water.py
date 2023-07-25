# Dynamic Programming Approach
# Time: O(n)
# Space: O(n)
# 2023.07.19: no
# notes: 用DP的方法，从两边开始，确认每个值最高值
class Solution(object):
    def trap(self, height):
        if not height:
            return 0

        ans = 0
        size = len(height)
        left_max = [0] * size
        right_max = [0] * size

        left_max[0] = height[0]
        for i in range(1, size):
            left_max[i] = max(height[i], left_max[i - 1])

        right_max[size - 1] = height[size - 1]
        for i in range(size - 2, -1, -1):
            right_max[i] = max(height[i], right_max[i + 1])

        for i in range(1, size - 1):
            ans += min(left_max[i], right_max[i]) - height[i]

        return ans

# Using 2 pointers Approach (best approach)
# Time: O(n)
# Space: O(1)
# 2023.07.19: no
# notes: 从两边往中间走，都从0开始，高的那边就停，让另一边走，注意点，left和right max的update是在比另一边大了之后进行，不是
# 一开始遇到今直接update，所以最高点不一定update到
class Solution2(object):
    def trap(self, height):
        left = 0
        right = len(height) - 1
        ans = 0
        left_max = 0
        right_max = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    ans += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    ans += right_max - height[right]
                right -= 1

        return ans

# stack Approach
# Time: O(n)
# Space: O(n)
# 2023.07.19: no
# notes: still confused
class Solution3(object):
    def trap(self, height):
        ans = 0
        current = 0
        st = []

        while current < len(height):
            while st and height[current] > height[st[-1]]:
                top = st.pop()
                if not st:
                    break
                distance = current - st[-1] - 1
                bounded_height = min(height[current], height[st[-1]]) - height[top]
                ans += distance * bounded_height

            st.append(current)
            current += 1

        return ans

# Tests:
test = Solution3()
test.trap([0,1,0,2,1,0,1,3,2,1,2,1])
