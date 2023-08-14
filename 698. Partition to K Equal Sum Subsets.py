# Backtracking
# Time: O(k2^n)
# Space: O(n)
# 2023.08.01: no
# notes: 以数字的视角，要不要装进某个桶， sort可以剪枝，并且用数组记录这个数字有没有被取过，可以跳过
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k > len(nums):
            return False
        sum_num = sum(nums)
        if sum_num % k != 0:
            return False
        else:
            target = sum_num // k
        bucket = [0]*k
        nums.sort(reverse=True)
        def backtrack(nums, index, bucket, target):
            if index == len(nums):
                for i in range(len(bucket)):
                    if bucket[i] != target:
                        return False
                return True
            for i in range(len(bucket)):
                if bucket[i] + nums[index] > target:
                    continue
                bucket[i] += nums[index]
                if backtrack(nums, index+1, bucket, target):
                    return True
                bucket[i] -= nums[index]
            return False
        return backtrack(nums, 0, bucket, target)

# Backtracking
# Time: O(n^2)
# Space: O(n)
# 2023.08.01: no
# notes: 用桶的视角做backtracking，正好填满一个桶之后才考虑装下一个桶
class Solution2(object):
    def canPartitionKSubsets(self, nums, k):
        # 排除一些基本情况
        if k > len(nums):
            return False
        total_sum = sum(nums)
        if total_sum % k != 0:
            return False
        used = [False] * len(nums)
        target = total_sum // k
        # k 号桶初始什么都没装，从 nums[0] 开始做选择
        def backtrack(k, bucket, nums, start, used, target):
            if k == 0:
                return True
            if bucket == target:
                return backtrack(k - 1, 0, nums, 0, used, target)
            for i in range(start, len(nums)):
                if used[i]:
                    continue
                if bucket + nums[i] > target:
                    continue
                used[i] = True
                if backtrack(k, bucket + nums[i], nums, i + 1, used, target):
                    return True
                used[i] = False
            return False
        return backtrack(k, 0, nums, 0, used, target)

# Backtracking
# Time: O(n^2)
# Space: O(n)
# 2023.08.01: no
# notes: 用桶的视角做backtracking，正好填满一个桶之后才考虑装下一个桶
# 为了防止多次重复计算，考虑用used number来计算用过的数字，用位运算方法，暂时跳过
class Solution3:
    def canPartitionKSubsets(self, nums, k):
        memo = {}

        def backtrack(k, bucket, nums, start, used, target):
            # 基本 case
            if k == 0:
                # 所有桶都被装满了，且 nums 全部用完
                return True
            if bucket == target:
                res = backtrack(k - 1, 0, nums, 0, used, target)
                # 缓存结果
                memo[used] = res
                return res
            if used in memo:
                # 避免冗余计算
                return memo[used]

            for i in range(start, len(nums)):
                if ((used >> i) & 1) == 1:
                    # nums[i] 已经被装入别的桶中
                    continue
                if nums[i] + bucket > target:
                    continue
                used |= 1 << i
                bucket += nums[i]
                if backtrack(k, bucket, nums, i + 1, used, target):
                    return True
                used ^= 1 << i
                bucket -= nums[i]

            return False

        # 确保 k 不大于 nums 的长度
        if k > len(nums):
            return False
        sum_nums = sum(nums)
        if sum_nums % k != 0:
            return False
        used = 0  # 使用位图技巧
        target = sum_nums // k  # 每个桶的目标和
        # k 号桶初始什么都没装，从 nums[0] 开始做选择
        return backtrack(k, 0, nums, 0, used, target)


# Tests:
test = Solution2()
test.canPartitionKSubsets(nums = [4,3,2,3,5,2,1], k = 4)
