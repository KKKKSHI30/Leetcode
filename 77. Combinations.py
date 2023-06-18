class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        cur = []
        results = []
        first = 1
        self.recursion(n, k, first, cur, results)
        return results

    def recursion(self, n, k, first, cur, results):
        if len(cur) == k:
            results.append(cur[:])
        for i in range(first, n+1):
            cur.append(i)
            self.recursion(n, k, i + 1, cur, results)
            cur.pop()

test = Solution()
test.combine(3, 3)
test.combine(4, 2)
test.combine(1, 1)
test.combine(5, 1)


class Solution2:
    def combine(self, n: int, k: int):
        # init first combination
        nums = list(range(1, k + 1)) + [n + 1]

        output, j = [], 0
        while j < k:
            # add current combination
            output.append(nums[:k])
            # increase first nums[j] by one
            # if nums[j] + 1 != nums[j + 1]
            j = 0
            while j < k and nums[j + 1] == nums[j] + 1:
                nums[j] = j + 1
                j += 1
            nums[j] += 1

        return output

test = Solution2()
test.combine(5, 3)
