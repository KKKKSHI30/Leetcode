# Math
# Time: O(logn)
# Space: O(1)
# 2023.08.17: yes
class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        res = []
        unique = False
        for i in range(1,n+1):
            if i*i == n:
                res.append(i)
                unique = True
                break
            elif i*i > n:
                break
            if n % i == 0:
                res.append(i)
        if k-1 < len(res):
            return res[k-1]
        elif unique:
            if len(res) * 2 - k - 1 < 0:
                return -1
            return int(n / res[len(res) * 2 - k - 1])
        else:
            if len(res) * 2 - k <0:
                return -1
            return int(n/res[len(res)*2-k])

# notes: 写的更简单
class Solution2:
    def kthFactor(self, n: int, k: int) -> int:
        divisors, sqrt_n = [], int(n ** 0.5)
        for x in range(1, sqrt_n + 1):
            if n % x == 0:
                k -= 1
                divisors.append(x)
                if k == 0:
                    return x

        # If n is a perfect square
        # we have to skip the duplicate
        # in the divisor list
        if (sqrt_n * sqrt_n == n):
            k += 1

        n_div = len(divisors)
        return n // divisors[n_div - k] if k <= n_div else -1

# Tests:
test = Solution2()
test.kthFactor(4,4)
test.kthFactor(7,2)
test.kthFactor(12,3)