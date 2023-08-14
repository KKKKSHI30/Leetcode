import math
from collections import Counter, defaultdict
class Solution(object):
    def minimumSeconds(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = Counter(nums)
        results = float("inf")
        for word, cnt in c.most_common():
            cur_array = [index for index, value in enumerate(nums) if value == word]
            distance = float("-inf")
            if results * 2 * cnt + 1 < len(nums):
                return results
            if cnt >= 2:
                for i in range(len(cur_array)):
                    if i == len(cur_array)-1:
                        distance = max(len(nums)-1-cur_array[i] + cur_array[0], distance)
                    else:
                        distance = max(cur_array[i+1] - cur_array[i]-1, distance)
                results = min(results, math.ceil(distance / 2))
            else:
                results = min(results, math.ceil((len(nums)-1)/2))
        return results


# notes: 长度*2，记录前一个节点即可
class Solution2:
    def minimumSeconds(self, nums):
        pos, gap = {}, defaultdict(lambda: 0)
        for i, n in enumerate(nums + nums):
            if n in pos:
                gap[n] = max(gap[n], (i - pos[n]) // 2)
            pos[n] = i
        return min(gap.values())


# Tests:
test = Solution2()
test.minimumSeconds([5,5,5,5])
test.minimumSeconds([2,1,3,3,2])
test.minimumSeconds([1,2,3,4,5])
test.minimumSeconds([1,2,1,2])




