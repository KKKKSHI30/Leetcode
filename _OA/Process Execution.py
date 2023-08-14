"""
题目简介：找出数组输出的最大和， 条件如果选择nums[x] 则不可以选择nums[x] - 1 & nums[x] + 1.
例： nums[1,2,2,3,3,3, 8] =》maxSum = 1+3+3+3+8
Tag： Dynamic Programming
思路：
    首先找出重复数字 并加和 再添加如hashMap（powers）当中，上述例子中例{ {1: 1}  { 2 : 4} { 3 : 9} { 8 : 8} }
    Recursive function:
        对于某个值num来说两种情况： 1）要这个值： powers[num] + maxPoins(num - 2)
                                                           2) 不要这个值：maxPoins(num - 1)
         返回上述两种情况max即可
         base case: num == 0 return 0
                           num == 1 return powers[1]
"""
# recursive way
def maxPoints_recursive(nums):
    if nums == None:
        return 0
    individual_sum = {}
    for num in nums:
        individual_sum[num] = individual_sum.get(num, 0) + num
    memo = {}
    def maxSum(position):
        if position <= 0:
            return 0
        if position in memo:
            return memo[position]
        take_num = individual_sum.get(position, 0) + maxSum(position - 2)
        skip_num = maxSum(position - 1)
        memo[num] = max(take_num, skip_num)
        return memo[num]
    return maxSum(max(nums))

# iterative way
def maxPoints(power):
    if not power:
        return 0
    num_sum = {}
    for num in power:
        num_sum[num] = num_sum.get(num, 0) + num
    max_num = max(power)
    memo = [0] * (max_num + 1)
    memo[1] = num_sum.get(1, 0)
    for num in range(2, max_num + 1):
        memo[num] = max(num_sum.get(num, 0) + memo[num - 2], memo[num - 1])
    return memo[max_num]

# Example usage:
max_sum = maxPoints([1,2,2,3,3,3,7,8])
max_sum2 = maxPoints([1,2,3,4,5])
max_sum3 = maxPoints([1,1,1,2])
max_sum4 = maxPoints([2,2,2,3])
