class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        results = []
        cur = []
        start = 0
        self.backtracking(candidates, cur, target, results, start)
        return results

    def backtracking(self, candidates, cur, target, results, start):
        if sum(cur) == target:
            results.append(cur[:])
            return
        elif sum(cur) > target:
            return
        for i in range(start, len(candidates)):
            cur.append(candidates[i])
            self.backtracking(candidates, cur, target, results, i)
            cur.pop()

test = Solution()
test.combinationSum([2,3,6,7], 7)
