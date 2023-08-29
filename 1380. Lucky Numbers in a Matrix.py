# Recursion
# Time: O(mn)
# Space: O(1)
# 2023.08.14: no
# notes: 时间复杂度高了不难，就是全部检查一遍，但是这道题O(1)的话，就很难理解了
# 1. 一个Matrix中不可能存在两个lucky number
# 2. 所以找到所有行最小值的最大值和所有列的最大值的最小值，看看匹配不配即可
import math
class Solution:
    def luckyNumbers(self, matrix):
        # max of row min
        maxMin = -math.inf
        # min of max col
        minMax = math.inf
        for row in range(len(matrix)):
            maxMin = max(maxMin, min(matrix[row]))
        for col in zip(*matrix):
            minMax = min(minMax, max(col))
        return [maxMin] if maxMin == minMax else []

# Tests:
test = Solution()
test.luckyNumbers([[3,7,8],[9,11,13],[15,16,17]])