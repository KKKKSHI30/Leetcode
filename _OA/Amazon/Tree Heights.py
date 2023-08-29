# 题目： https://leetcode.com/discuss/interview-question/1171979/a-good-question-of-amazon-sde
def solve(nums, X):
    N = len(nums)
    minn = min(nums)
    # Observe that making any element of our array less than the minimum or more than maximum would result in extra useless operation, hence j can be in the range of [min(nums), max(nums)], both inclusive. Here we can subtract min values from each element in array just to make the code more readable
    for i in range(len(nums)):
        nums[i] -= minn
    maxn = max(nums) + 1

    # dp[i][j] is the minimum number of operations required to make nums[:i+1](till ith index) strictly sorted with nums[i] == j.
    # Hence, our recurrence relation would be: dp[i][j] = abs(nums[i]-j) + min(dp[i-1][:j])
    # This 2D table can be easily converted to 1D dp[j], since we only ever need to know the i-1th state for computing ith state.
    dp = [[float('inf')] * (maxn) for _ in range(N)]

    # Initialize base case
    for j in range(maxn):
        dp[0][j] = abs(nums[0] - j)

    for i in range(1, len(nums)):
        min_so_far = min(dp[i - 1][:i])
        for j in range(i, maxn):  # starting from i to ensure strictly increasing order
            dp[i][j] = abs(nums[i] - j) + min_so_far
            min_so_far = min(min_so_far, dp[i - 1][j])
    return "YES " + str(min(dp[-1])) if min(dp[-1]) <= X else "NO"


def main():
    import sys

    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            arr = eval(next(lines))
            X = eval(next(lines))
            print(solve(arr, X))
        except StopIteration:
            break


if __name__ == '__main__':
    main()