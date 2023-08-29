class Solution:
    def __init__(self):
        self.s = ""
        self.k = 0
        self.dp = []

    def numberOfBeautifulIntegers(self, low, high, k):
        self.k = k
        self.s = str(low - 1)
        self.dp = [[[[[-1 for _ in range(21)] for _ in range(21)] for _ in range(2)] for _ in range(2)] for _ in range(len(self.s))]
        l = self.f(0, True, True, 0, 0)

        self.s = str(high)
        self.dp = [[[[[-1 for _ in range(21)] for _ in range(21)] for _ in range(2)] for _ in range(2)] for _ in range(len(self.s))]
        h = self.f(0, True, True, 0, 0)
        return h - l

    def f(self, i, bound, isZero, cnt, rem):
        if i == len(self.s):
            if cnt == 0 and rem == 0:
                return 1
            return 0

        if self.dp[i][int(bound)][int(isZero)][cnt + 10][rem] != -1:
            return self.dp[i][int(bound)][int(isZero)][cnt + 10][rem]

        max_val = 9

        if bound:
            max_val = int(self.s[i])

        ans = 0
        for j in range(max_val + 1):
            new_cnt = cnt
            if not isZero or j > 0:
                new_cnt += (1 if j % 2 == 0 else -1)
            ans += self.f(i + 1, bound and j == max_val, isZero and j == 0, new_cnt, (rem * 10 + j) % self.k)
        self.dp[i][int(bound)][int(isZero)][cnt + 10][rem] = ans
        return ans