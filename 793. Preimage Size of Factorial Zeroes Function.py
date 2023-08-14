# Counting Factors of 5 Efficiently
# Time: O(logn)
# Space: O(1)
# 2023.08.04: yes
# notes: 用binary search的方法来判断边界，上边界需要*10是因为*10才会多一个0，*5是不行的，在zeta中不对
class Solution:
    def preimageSizeFZF(self, K):

        def zeta(x):
            return x // 5 + zeta(x // 5) if x > 0 else 0

        lo, hi = K, 10 * K + 1
        while lo < hi:
            mi = (lo + hi) // 2
            zmi = zeta(mi)

            if zmi == K:
                return 5
            elif zmi < K:
                lo = mi + 1
            else:
                hi = mi

        return 0

# Tests:
test = Solution()
test.preimageSizeFZF(5)