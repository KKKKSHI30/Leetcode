# Bit Manipulation
# Time: O(1)
# Space: O(1)
# 2023.08.02: yes
# notes: 用到的技巧是n & n-1可以提取最后一位1
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        if n < 0:
            return False
        while n != 0:
            n = n & (n - 1)
            count += 1
        return count == 1

# Bit Manipulation
# Time: O(1)
# Space: O(1)
# 2023.08.02: yes
# notes: 用n & n-1把最后一位1去掉之后，看剩下的是不是0就行了
class Solution2(object):
    def isPowerOfTwo(self, n):
        if n == 0:
            return False
        return n & (n - 1) == 0

# Bit Manipulation
# Time: O(1)
# Space: O(1)
# 2023.08.02: no
# notes: 用的技巧是n & -n只会保留最右边的一位1，如果这个数字只有一个1，那就会等于他自己
# 否则就 不等
class Solution3(object):
    def isPowerOfTwo(self, n):
        if n == 0:
            return False
        return n & (-n) == n

test = Solution()
test.isPowerOfTwo(-16)
test.isPowerOfTwo(1)
test.isPowerOfTwo(9)

