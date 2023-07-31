# Dynamic Programming
# Time: O(n)
# Space: O(1)
# 2023.07.29: yes
# notes: 4D DP，等dp好顺利的时候来看吧，现在难度还是高了点，不过分享一下思路，主要是根据下面的youtube视频
# https://www.youtube.com/watch?v=ypPHL72ch4Q
# 1. 最开始的数字是不是0，是的话，这个数字还没开始
# 2. 这个数字是不是和上限的边界一样，一样的话，证明数字不能选0-9，而是要有选择性的
# 3. 当前数字是什么，下一个数字，只能+1或者-1来确定是stepping number
# 4. 当前是第几个数字
# 这个DP是改变状态的，稍微对DP又加深了一点印象吧，倒不全是1，2状态的改变，有可能是多样性的
# 而且有些是0，1的状态改变
from functools import cache
MOD = int(1e9) + 7
class Solution:
    def _count(self, n: str) -> int:  # count number of stepping numbers in range [0...n]
        @cache
        def dp(i, tight, lastDigit, leadingZero):
            if i == len(n): return 1  # Found a good number
            maxDigit = int(n[i]) if tight else 9
            ans = 0
            for d in range(maxDigit + 1):
                nxtTight = tight and d == maxDigit
                nxtLeadingZero = leadingZero and d == 0
                if nxtLeadingZero:  # for leading zero, we shouldn't treat lastDigit=d
                    ans = (ans + dp(i + 1, nxtTight, lastDigit, nxtLeadingZero)) % MOD
                elif lastDigit == -1 or abs(lastDigit - d) == 1:
                    ans = (ans + dp(i + 1, nxtTight, d, nxtLeadingZero)) % MOD
            return ans
        return dp(0, True, -1, True)
    def _minusOne(self, s): # s is a string representing a positive integer
        num = int(s) - 1
        return str(num)
    def countSteppingNumbers(self, low: str, high: str) -> int:
        return (self._count(high) - self._count(self._minusOne(low)) + MOD) % MOD

# Test:
test = Solution()
test.countSteppingNumbers(low = "90", high = "101")
