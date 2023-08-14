# Bit Manipulation
# Time: O(1)
# Space: O(1)
# 2023.08.02: yes
# notes: 用到的技巧是n & n-1可以提取最后一位1
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n != 0:
            n = n & (n - 1)
            count += 1
        return count

# Bit Manipulation
# Time: O(n^2)
# Space: O(n)
# 2023.08.02: no
# notes: 用一个bit mask来确认
class Solution2(object):
    def hammingWeight(n):
        bits = 0
        mask = 1
        for i in range(32):
            if n & mask != 0:
                bits += 1
            mask <<= 1
        return bits


# Tests:
test = Solution()
test.hammingWeight(n = 0b00000000000000000000000000001011)