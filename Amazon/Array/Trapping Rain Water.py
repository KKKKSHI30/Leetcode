import copy

# piece of shit
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 2:
            return 0
        saving = 0
        height2 = copy.deepcopy(height)
        height2.sort()
        second_max_height = height2[-2]
        for i in range(1, second_max_height +1):
            left = -1
            right = 0
            for j in range(len(height)):
                if height[j] >= i and left == -1:
                    left = j
                elif height[j] >= i:
                    right = j
                    saving += right - left - 1
                    left = right
        return saving

# piece of shit too
class Solution2(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 2:
            return 0
        height2 = copy.deepcopy(height)
        def max_two(height):
            height.sort(reverse=True)
            return height[1]
        max_two_height = max_two(height2)
        if max_two_height < 1:
            return 0
        water = 0
        max_height = 1
        check = False
        for i in range(len(height)-1):
            if height[i] >= max_height and height[i] <= max(height[i+1:]):
                max_height = height[i]
                check = True
            elif height[i] >= max_height and height[i] >= max(height[i+1:]):
                max_height = max(height[i+1:])
                check = True
            elif check:
                water += max_height - height[i]
        return water


class Solution2:  # go over two times, one from left max and one for right max
    def trap(self, height):
        n = len(height)
        maxLeft, maxRight = [0] * n, [0] * n

        for i in range(1, n):
            maxLeft[i] = max(height[i - 1], maxLeft[i - 1])
        for i in range(n - 2, -1, -1):
            maxRight[i] = max(height[i + 1], maxRight[i + 1])

        ans = 0
        for i in range(n):
            waterLevel = min(maxLeft[i], maxRight[i])
            if waterLevel >= height[i]:
                ans += waterLevel - height[i]
        return ans

# tips: using double pointer and assume left is always smaller than right to calculate water
class Solution3:  # 48 ms, faster than 92.74%
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2: return 0
        n = len(height)
        maxLeft, maxRight = height[0], height[n-1]
        left, right = 1, n - 2
        ans = 0
        while left <= right:
            if maxLeft < maxRight:
                if height[left] > maxLeft:
                    maxLeft = height[left]
                else:
                    ans += maxLeft - height[left]
                left += 1
            else:
                if height[right] > maxRight:
                    maxRight = height[right]
                else:
                    ans += maxRight - height[right]
                right -= 1
        return ans


test = Solution()
test.trap([0,1,0,2,1,0,1,3,2,1,2,1])
test.trap([4,2,0,3,2,5])
test.trap([2,0,2])
test.trap([4,2,3])

