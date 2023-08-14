# Pop Count
# Time: O(nlogn)
# Space: O(1)
# 2023.08.02: yes
# notes: 循环一遍，每一个都走一遍需要多少个1
class Solution:
    def countBits(self, n):

        def pop_count(x):
            count = 0
            while x != 0:
                x &= x - 1  # zeroing out the least significant nonzero bit
                count += 1
            return count

        ans = [0] * (n + 1)
        for x in range(n + 1):
            ans[x] = pop_count(x)

        return ans

# DP + Most Significant Bit
# Time: O(n)
# Space: O(1)
# 2023.08.02: yes
# notes: dp的规定是generate [b, 2b) or [b, n) from [0, b)，因为左移一位就是*2，左移后的内容可以根据前面算出来
class Solution2:
    def countBits(self, n):
        ans = [0] * (n + 1)
        x = 0
        b = 1

        # [0, b) is calculated
        while b <= n:
            # generate [b, 2b) or [b, n) from [0, b)
            while x < b and x + b <= n:
                ans[x + b] = ans[x] + 1
                x += 1
            x = 0  # reset x
            b <<= 1  # b = 2b

        return ans


# DP + Least Significant Bit
# Time: O(n)
# Space: O(1)
# 2023.08.02: yes
# notes: 一个数也可以被，除二的1的个数，因为右移就差一个1，然后and一下1，就可以确定最后一位是不是1
class Solution3:
    def countBits(self, n):
        ans = [0] * (n + 1)
        for x in range(1, n + 1):
            # x // 2 is x >> 1 and x % 2 is x & 1
            ans[x] = ans[x >> 1] + (x & 1)
        return ans


# DP + Last Set Bit
# Time: O(n)
# Space: O(1)
# 2023.08.02: yes
# notes: 根据x&x-1消除的最后一位1，得到前面的值，然后加上1就行了，神作
class Solution4:
    def countBits(self, n):
        ans = [0] * (n + 1)
        for x in range(1, n + 1):
            ans[x] = ans[x & (x - 1)] + 1
        return ans

# Tests:
test = Solution3()
test.countBits(12)