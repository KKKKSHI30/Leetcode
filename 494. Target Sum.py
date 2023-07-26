# Bottom Up Dynamic Programming
# Time: O(tn)
# Space: O(tn)
# 2023.07.25: no
# notes: dp[i][j] refers to the number of assignments which can lead to a sum of j up to the ith index
class Solution:
    def findTargetSumWays(self, nums, S):
        total = sum(nums)
        dp = [[0] * (2 * total + 1) for _ in range(len(nums))]
        dp[0][nums[0] + total] = 1
        dp[0][-nums[0] + total] += 1

        for i in range(1, len(nums)):
            for s in range(-total, total + 1):
                if dp[i - 1][s + total] > 0:
                    # 这个次数不会变化，因为一共只有2^n的种方法，这个意思其实就是把dp[i-1][s+total]的次数变化到
                    # dp[i][s + nums[i] + total]，加过这个数字上，数字本身不会变化，由多条路径加起来才会变化
                    dp[i][s + nums[i] + total] += dp[i - 1][s + total]
                    dp[i][s - nums[i] + total] += dp[i - 1][s + total]
        return 0 if abs(S) > total else dp[len(nums) - 1][S + total]


# Backtracking
# Time: O(2^n)
# Space: O(1)
# 2023.07.25: no
# notes: 只是提供一种思路，超时
class Solution2:
    def __init__(self):
        self.result = 0
    def findTargetSumWays(self, nums, target):
        if len(nums) == 0:
            return 0
        self.backtrack(nums, 0, target)
        return self.result
    def backtrack(self, nums, i, remain):
        if i == len(nums):
            if remain == 0:
                self.result += 1
            return
        remain += nums[i]
        self.backtrack(nums, i + 1, remain)
        remain -= nums[i]
        remain -= nums[i]
        self.backtrack(nums, i + 1, remain)
        remain += nums[i]


# Recursion，非标答
# Time: O(tn)
# Space: O(tn)
# 2023.07.25: no
# notes: 用str记录
class Solution3:
    def findTargetSumWays(self, nums, target):
        if len(nums) == 0:
            return 0
        memo = {}
        def dp(i, remain):
            # base case
            if i == len(nums):
                if remain == 0:
                    return 1
                return 0
            # 把它俩转成字符串才能作为哈希表的键
            key = str(i) + "," + str(remain)
            if key in memo:
                return memo[key]
            result = dp(i + 1, remain - nums[i]) + dp(i + 1, remain + nums[i])
            memo[key] = result
            return result
        return dp(0, target)


# Recursion 标答
# Time: O(tn)
# Space: O(tn)
# 2023.07.25: no
# notes: memo[i][sum + self.total] = add + subtract这句话的意思是，add这条支线上返回的次数+subtract返回的次数，即为所有次数
class Solution4:
    def __init__(self):
        self.total = 0

    def findTargetSumWays(self, nums, S):
        self.total = sum(nums)
        memo = [[float('-inf')] * (2 * self.total + 1) for _ in range(len(nums))]
        return self.calculate(nums, 0, 0, S, memo)

    def calculate(self, nums, i, sum, S, memo):
        if i == len(nums):
            if sum == S:
                return 1
            else:
                return 0
        else:
            if memo[i][sum + self.total] != float('-inf'):
                return memo[i][sum + self.total]
            add = self.calculate(nums, i + 1, sum + nums[i], S, memo)
            subtract = self.calculate(nums, i + 1, sum - nums[i], S, memo)
            memo[i][sum + self.total] = add + subtract
            return memo[i][sum + self.total]

# 1D Dynamic Programming
# Time: O(tn)
# Space: O(t)
# 2023.07.25: no
class Solution5:
    def __init__(self):
        self.total = 0

    def findTargetSumWays(self, nums, S):
        self.total = sum(nums)
        memo = [[float('-inf')] * (2 * self.total + 1) for _ in range(len(nums))]
        return self.calculate(nums, 0, 0, S, memo)

    def calculate(self, nums, i, sum, S, memo):
        if i == len(nums):
            if sum == S:
                return 1
            else:
                return 0
        else:
            if memo[i][sum + self.total] != float('-inf'):
                return memo[i][sum + self.total]
            add = self.calculate(nums, i + 1, sum + nums[i], S, memo)
            subtract = self.calculate(nums, i + 1, sum - nums[i], S, memo)
            memo[i][sum + self.total] = add + subtract
            return memo[i][sum + self.total]



test = Solution4()
test.findTargetSumWays([1,1,1,1,1], 3)


