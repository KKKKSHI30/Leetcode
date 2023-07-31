# Dynamic Programming
# Time: O(nk)
# Space: O(nk)
# 2023.07.28: yes
# 参考神中神六六归一算法
# https://labuladong.github.io/algo/di-er-zhan-a01c6/yong-dong--63ceb/yi-ge-fang-3b01b/
# base case：
# dp[-1][...][0] = dp[...][0][0] = 0
# dp[-1][...][1] = dp[...][0][1] = -infinity
# 状态转移方程：
# dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
# dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
import math
class Solution:
    def maxProfit(self, k, prices):
        n = len(prices)
        max_k = min(n // 2, k)
        dp = [[[0] * 2 for _ in range(max_k + 1)] for _ in range(n)]
        """
        k = 0 时的 base case，因为后面都会替代掉，所以不写也没关系
        for i in range(n):
            dp[i][0][1] = -float("inf")
            dp[i][0][0] = 0
        """
        for i in range(n):
            for k in range(max_k, 0, -1):
                if i - 1 == -1:
                    # 处理 base case
                    dp[i][k][0] = 0
                    dp[i][k][1] = -prices[i]
                    continue
                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])
        # 穷举了 n × max_k × 2 个状态，正确。
        return dp[n - 1][max_k][0]

# Merging
# Time: O(n(n-k))
# Space: O(n)
# 2023.07.28: yes
# notes: 这个思路是根据k = inf倒推回来的，首先列出所有增长的，再看符不符合小于k的条件，如果符合，直接返回max即可
# 如果不符合，就需要考虑merge或者drop，merge的话和Meeting room感觉很像，找到profit最小的情况
# 如果merge的profit更大就merge，否则则drop
class Solution2:
    def maxProfit(self, k: int, prices) -> int:
        n = len(prices)
        # solve special cases
        if not prices or k == 0:
            return 0
        # find all consecutively increasing subsequence
        transactions = []
        start = 0
        end = 0
        for i in range(1, n):
            if prices[i] >= prices[i-1]:
                end = i
            else:
                if end > start:
                    transactions.append([start, end])
                start = i
        if end > start:
            transactions.append([start, end])
        while len(transactions) > k:
            # check delete loss
            delete_index = 0
            min_delete_loss = math.inf
            for i in range(len(transactions)):
                t = transactions[i]
                profit_loss = prices[t[1]] - prices[t[0]]
                if profit_loss < min_delete_loss:
                    min_delete_loss = profit_loss
                    delete_index = i
            # check merge loss
            merge_index = 0
            min_merge_loss = math.inf
            for i in range(1, len(transactions)):
                t1 = transactions[i-1]
                t2 = transactions[i]
                profit_loss = prices[t1[1]] - prices[t2[0]]
                if profit_loss < min_merge_loss:
                    min_merge_loss = profit_loss
                    merge_index = i
            # delete or merge
            if min_delete_loss <= min_merge_loss:
                transactions.pop(delete_index)
            else:
                transactions[merge_index - 1][1] = transactions[merge_index][1]
                transactions.pop(merge_index)
        return sum(prices[j]-prices[i] for i, j in transactions)
# Tests:
test = Solution2()
test.maxProfit(k = 2, prices = [3,2,6,5,0,3,4,6,2,5,8,1,9])