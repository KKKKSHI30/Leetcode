# Bit by Bit
# Time: O(1)
# Space: O(1)
# 2023.08.02: yes
# notes: and 1 然后右移，循环往复
class Solution:
    def reverseBits(self, n):
        ret, power = 0, 31
        while n:
            ret += (n & 1) << power
            n = n >> 1
            power -= 1
        return ret

# Byte by Byte with Memoization
# Time: O(1)
# Space: O(1)
# 2023.08.02: yes
# notes: (byte * 0x0202020202 & 0x010884422010) % 1023是一个公式，就是把一个byte里面的bit逆转过来
# 这道题的思路是，先把Byte和byte转过来，再把每个Byte中的bit逆转过来
# 网址是: http://graphics.stanford.edu/~seander/bithacks.html#ReverseByteWith64BitsDiv
class Solution2:
    def reverseBits(self, n):
        ret, power = 0, 24
        cache = dict()
        while n:
            ret += self.reverseByte(n & 0xff, cache) << power
            n = n >> 8
            power -= 8
        return ret

    def reverseByte(self, byte, cache):
        if byte not in cache:
            cache[byte] = (byte * 0x0202020202 & 0x010884422010) % 1023
        return cache[byte]


# Mask and Shift
# Time: O(1)
# Space: O(1)
# 2023.08.02: yes
# notes: https://leetcode.com/problems/reverse-bits/editorial/
# 标答的图画的非常清晰，哪怕我根本不知道下面这一坨东西是什么，思路大概是把32bit分成16，然后交换16
# 分成8，,8，交换8，8，分成4，4交换以此类推
class Solution3:
    def reverseBits(self, n):
        n = (n >> 16) | (n << 16)
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
        return n

# Tests:
test = Solution()
test.reverseBits()