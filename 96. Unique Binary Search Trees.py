# Dynamic Programming Approach
# Time: O(logn)
# Space: O(h)
# 2023.06.30: no
# notes: 动规，建议以后重看一遍，明白思路，但是不会写，核心只有一句话，res = left*right，其他都是初始化+保存递归的过程
class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        G = [0]*(n+1)
        G[0], G[1] = 1, 1

        for i in range(2, n+1):
            for j in range(1, i+1):
                left = j-1
                right = i-j
                G[i] += G[left] * G[right]
        return G[n]

# Recursion Approach
# Time: O(n^2)
# Space: O(n)
# 2023.06.30: no
class Solution2(object):
    def numTrees(self, n):
        # Initialize memo with 0 values
        self.memo = [[0] * (n + 1) for _ in range(n + 1)]
        return self.count(1, n)

    def count(self, lo, hi):
        if lo > hi:
            return 1
        # Check the memoization table
        if self.memo[lo][hi] != 0:
            return self.memo[lo][hi]

        res = 0
        for mid in range(lo, hi + 1):
            left = self.count(lo, mid - 1)  # Fixed method call
            right = self.count(mid + 1, hi)  # Fixed method call
            res += left * right   # 核心
        # Store the result in the memoization table
        self.memo[lo][hi] = res

        return res

# Mathematical Deduction Approach
# Time: O(n)
# Space: O(1)
# 2023.06.30: yes
class Solution2(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        C = 1
        for i in range(0, n):
            C = C * 2*(2*i+1)/(i+2)
        return int(C)

# Tests:
test = Solution()
test.numTrees(3)