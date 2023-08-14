# Fisher-Yates Algorithm
# Time: O(n)
# Space: O(n)
# 2023.08.04: no
# notes: Fisher-Yates Algorithm，也被成为洗牌算法，第一个元素n个可能性，第二个元素n-1，以此类推
# 可能性是n!，所以正确
import random
class Solution:
    def __init__(self, nums):
        self.nums = nums
        self.rand = random.Random()

    def reset(self):
        return self.nums

    # 洗牌算法
    def shuffle(self):
        n = len(self.nums)
        copy = self.nums.copy()
        for i in range(n):
            # 生成一个 [i, n-1] 区间内的随机数
            r = i + self.rand.randint(0, n - i - 1)
            # 交换 nums[i] 和 nums[r]
            copy[i], copy[r] = copy[r], copy[i]
        return copy

# Tests:
obj = Solution([1,2,3])
param_1 = obj.reset()
param_2 = obj.shuffle()

# Backtracking
# Time: O(n^2)
# Space: O(n)
# 2023.08.04: no
# notes: 从array中随机找一个number，然后放到new_array中，一个个放就是随机的
class Solution:
    def __init__(self, nums):
        self.array = nums
        self.original = list(nums)

    def reset(self):
        self.array = self.original
        self.original = list(self.original)
        return self.array

    def shuffle(self):
        aux = list(self.array)

        for idx in range(len(self.array)):
            remove_idx = random.randrange(len(aux))
            self.array[idx] = aux.pop(remove_idx)

        return self.array