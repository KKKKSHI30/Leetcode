# Top Down Dynamic Programming (超时)
# Time: O(kn^2)
# Space: O(kn)
# 2023.07.27: no
# notes: 这个方法的dp是对于N层楼，有k个鸡蛋，最少人扔几次
# 这道题的两个方法，线性查找+二分查找
# base case如果n = 0, 不用扔了， return 0，如果k = 1，只能线性扔， return n
class Solution:
    def superEggDrop(self, K, N):
        # Memoization table
        memo = [[-666 for _ in range(N + 1)] for _ in range(K + 1)]
        return self.dp(K, N, memo)

    def dp(self, K, N, memo):
        # Base cases
        if K == 1:
            return N
        if N == 0:
            return 0

        # Check memoization table to avoid redundant calculations
        if memo[K][N] != -666:
            return memo[K][N]

        # State transition
        res = float('inf')
        for i in range(1, N + 1):
            # Try all floors and take the minimum attempts needed
            res = min(
                res,
                # Take the worst case scenario between egg breaks and doesn't break
                max(self.dp(K, N - i, memo), self.dp(K - 1, i - 1, memo)) + 1
            )

        # Store result in memoization table
        memo[K][N] = res
        return res

# Top down Dynamic Programming with Binary Search
# Time: O(knlogn)
# Space: O(kn)
# 2023.07.27: no
# notes: 动态转移方程：res = Math.min(res,Math.max(dp(K, N - i), dp(K - 1, i - 1)) + 1)
class Solution2:
    def superEggDrop(self, K, N):
        # Memoization table
        memo = [[-666 for _ in range(N + 1)] for _ in range(K + 1)]
        return self.dp(K, N, memo)

    def dp(self, K, N, memo):
        # Base cases
        if K == 1:
            return N
        if N == 0:
            return 0

        # Check memoization table to avoid redundant calculations
        if memo[K][N] != -666:
            return memo[K][N]

        # Binary search for optimal floor to drop the egg
        res = float('inf')
        lo, hi = 1, N
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            # Check both cases when the egg breaks and when it doesn't break
            broken = self.dp(K - 1, mid - 1, memo)
            not_broken = self.dp(K, N - mid, memo)
            # res = min(max(碎，没碎) + 1)
            if broken > not_broken:
                hi = mid - 1
                res = min(res, broken + 1)
            else:
                lo = mid + 1
                res = min(res, not_broken + 1)

        # Store result in memoization table
        memo[K][N] = res
        return res

# Bottom Up Dynamic Programming
# Time: O(knlogn)
# Space: O(kn)
# 2023.07.27: no
# notes: DP定义为有k个鸡蛋，尝试扔m次，最多可以到达n层楼
# dp[k][m] = dp[k][m - 1] + dp[k - 1][m - 1] + 1
# 解释： 无论你上楼还是下楼，总的楼层数 = 楼上的楼层数 + 楼下的楼层数 + 1（当前这层楼）
# 过于聪明，感觉真的想不到，比起上一个动态转移方程，简单太多
class Solution3:
    def superEggDrop(self, K, N):
        # Create the dp array (2D table)
        dp = [[0 for _ in range(N + 1)] for _ in range(K + 1)]

        # Base cases (already initialized as 0 in Python)
        # dp[0][..] = 0
        # dp[..][0] = 0

        m = 0
        # 寻找m的过程，如果看不懂的话就看labuladong的转移方程
        while dp[K][m] < N:
            m += 1
            for k in range(1, K + 1):
                dp[k][m] = dp[k][m - 1] + dp[k - 1][m - 1] + 1

        return m


# Dynamic Programming with Optimality Criterion
# Time: O(kn)
# Space: O(kn)
# 2023.07.27: no
# notes: 真的看不懂，update一下以后来看，前面已经耗了两小时了，真的看不下去了，猜一下和solution3很像
class Solution4:
    def superEggDrop(self, K: int, N: int) -> int:

        # Right now, dp[i] represents dp(1, i)
        dp = range(N+1)

        for k in range(2, K+1):
            # Now, we will develop dp2[i] = dp(k, i)
            dp2 = [0]
            x = 1
            for n in range(1, N+1):
                # Let's find dp2[n] = dp(k, n)
                # Increase our optimal x while we can make our answer better.
                # Notice max(dp[x-1], dp2[n-x]) > max(dp[x], dp2[n-x-1])
                # is simply max(T1(x-1), T2(x-1)) > max(T1(x), T2(x)).
                while x < n and max(dp[x-1], dp2[n-x]) > \
                                max(dp[x], dp2[n-x-1]):
                    x += 1

                # The final answer happens at this x.
                dp2.append(1 + max(dp[x-1], dp2[n-x]))

            dp = dp2
        return dp[-1]


# Mathematical
# Time: O(klogn)
# Space: O(1)
# 2023.07.27: no
# notes: mathematics，纯数证明，跳过
class Solution5:
    def superEggDrop(self, K: int, N: int) -> int:
        def f(x):
            ans = 0
            r = 1
            for i in range(1, K+1):
                r *= x-i+1
                r //= i
                ans += r
                if ans >= N: break
            return ans

        lo, hi = 1, N
        while lo < hi:
            mi = (lo + hi) // 2
            if f(mi) < N:
                lo = mi + 1
            else:
                hi = mi
        return lo

















