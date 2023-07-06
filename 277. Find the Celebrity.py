# Logical Deduction Approach
# Time: O(n)
# Space: O(n)
# 2023.07.04: yes
class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        q = []
        for i in range(n):
            q.append(i)
        while len(q) >= 2:
            cand = q.pop()
            other = q.pop()
            # cand 认识别人，cand不是，或者别人并不认识cand，cand也不是
            if knows(cand, other) or not knows(other, cand):
                # cand 不可能是名人，排除，让 other 归队
                q.insert(0, other)
            else:
                q.insert(0, cand)
        cand = q.pop()

        for other in range(n):
            if other == cand:
                continue
            # 保证其他人都认识 cand，且 cand 不认识任何其他人
            if not knows(other, cand) or knows(cand, other):
                return -1
        return cand


# Logical Deduction Approach
# Time: O(n)
# Space: O(n)
# 2023.07.04: yes
class Solution2(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        cand = 0
        for other in range(1, n):
            # cand 认识别人，cand不是，或者别人并不认识cand，cand也不是
            if knows(cand, other) or not knows(other, cand):
                cand = other
        for other in range(n):
            if other == cand:
                continue
            # 保证其他人都认识 cand，且 cand 不认识任何其他人
            if not knows(other, cand) or knows(cand, other):
                return -1
        return cand

# Logical Deduction with Caching
# Time: O(n)
# Space: O(n)
# 2023.07.04: no
# notes: 把knows cache一下，会快一点，不用重复调用api
from functools import lru_cache
class Solution3:
    @lru_cache(maxsize=None)
    def cachedKnows(self, a, b):
        return knows(a, b)
    def findCelebrity(self, n: int) -> int:
        self.n = n
        celebrity_candidate = 0
        for i in range(1, n):
            if self.cachedKnows(celebrity_candidate, i):
                celebrity_candidate = i
        if self.is_celebrity(celebrity_candidate):
            return celebrity_candidate
        return -1
    def is_celebrity(self, i):
        for j in range(self.n):
            if i == j: continue
            if self.cachedKnows(i, j) or not self.cachedKnows(j, i):
                return False
        return True


