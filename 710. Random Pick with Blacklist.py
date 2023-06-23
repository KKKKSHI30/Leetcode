# Virtual Whitelist Approach (best approach)
# Time: O(1)
# Space: O(1)
# 2023.06.22:no
from typing import List
import random

class Solution:
    def __init__(self, N: int, blacklist: List[int]):
        # 计算真实的数据个数
        self.sz = N - len(blacklist)
        # 用哈希表记录黑名单中的数据
        self.mapping = {}
        for b in blacklist:
            self.mapping[b] = 666

        # 处理黑名单中的数据，将其映射到其他位置
        last = N - 1
        for b in blacklist:
            if b >= self.sz:
                continue
            # 找到一个未被映射到的位置，将其作为映射目标
            while last in self.mapping:
                last -= 1
            # 将 b 映射到 last，并将 last 位置的数据映射到 b
            self.mapping[b] = last
            last -= 1

    def pick(self) -> int:
        # 随机生成一个索引
        index = random.randint(0, self.sz - 1)
        # 如果该索引对应的数据在黑名单中，返回其映射到的数据
        if index in self.mapping:
            return self.mapping[index]
        # 否则直接返回该索引
        return index



# Binary Search over Blacklist Approach
# Time: O(blogb)
# Space: O(b)
# 2023.06.22:no
import random

class Solution2:
    def __init__(self, N, blacklist):
        self.n = N
        blacklist.sort()
        self.b = blacklist

    def pick(self):
        k = random.randint(0, self.n - len(self.b) - 1)
        lo = 0
        hi = len(self.b) - 1

        while lo < hi:
            i = (lo + hi + 1) // 2
            if self.b[i] - i > k:
                hi = i - 1
            else:
                lo = i

        return k + lo + 1 if lo == hi and self.b[lo] - lo <= k else k


# Tests:
obj = Solution2(5, [2,4])
param_1 = obj.pick()
