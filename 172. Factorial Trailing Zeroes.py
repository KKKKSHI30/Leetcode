# Counting Factors of 5 Efficiently
# Time: O(logn)
# Space: O(1)
# 2023.08.04: yes
# notes: 判断有几个5，几个25， 几个125
class Solution:
    def trailingZeroes(self, n):
        res = 0
        divisor = 5
        while divisor <= n:
            res += n // divisor
            divisor *= 5
        return res

# Counting Factors of 5
# Time: O(n)
# Space: O(1)
# 2023.08.04: yes
class Solution2:
    def trailingZeroes(self, n):
        zero_count = 0
        for i in range(5, n + 1, 5):
            current = i
            while current % 5 == 0:
                zero_count += 1
                current //= 5

        return zero_count

# Tests:
test = Solution()
test.trailingZeroes(26)