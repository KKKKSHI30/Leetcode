# Brute Force
# Time: O(n)
# Space: O(n)
# 2023.08.04: no
# notes: 标答过不去
class Solution:
    def __init__(self, nums):
        # Do not allocate extra space for the nums array
        self.nums = nums
        self.rand = random.Random()

    def pick(self, target):
        indices = []
        n = len(self.nums)
        for i in range(n):
            if self.nums[i] == target:
                indices.append(i)
        l = len(indices)
        # pick an index at random
        random_index = indices[self.rand.randint(0, l - 1)]
        return random_index


# Caching results using a hashmap
# Time: O(n)
# Space: O(n)
# 2023.08.04: no
# notes: 完全不懂，标答中唯一过的
import random
from collections import defaultdict

class Solution2:
    def __init__(self, nums):
        self.rand = random.Random()
        self.indices = defaultdict(list)
        for i, num in enumerate(nums):
            self.indices[num].append(i)

    def pick(self, target):
        l = len(self.indices[target])
        # pick an index at random
        random_index = self.indices[target][self.rand.randint(0, l - 1)]
        return random_index

# Reservoir sampling
# Time: O(n)
# Space: O(n)
# 2023.08.04: no
# notes: 完全不懂，且标答超时
import random

class Solution3:
    def __init__(self, nums):
        self.nums = nums
        self.rand = random.Random()

    def pick(self, target):
        count = 0
        idx = 0
        for i, num in enumerate(self.nums):
            # if nums[i] is equal to target, i is a potential candidate
            # which needs to be chosen uniformly at random
            if num == target:
                # increment the count of total candidates
                # available to be chosen uniformly at random
                count += 1
                # we pick the current number with probability 1 / count (reservoir sampling)
                if self.rand.randint(1, count) == 1:
                    idx = i
        return idx

