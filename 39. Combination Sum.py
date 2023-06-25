# Backtracking (best approach)
# Time: O(n^(t/m+1)), t/m is height
# Space: O(t/m)
# 2023.06.24:
class Solution(object):
    # start 是起始 index
    def backtrack(self, candidates, results, combination, start, remain):
        if remain < 0:
            return results
        elif remain == 0:
            return results.append(combination[:]) # deep copy
        for i in range(start, len(candidates)):
            combination.append(candidates[i])
            self.backtrack(candidates, results, combination, i, remain-candidates[i])
            combination.pop()
        return results

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = self.backtrack(candidates, [], [], 0, target)
        return result


test = Solution()
test.combinationSum([2,3,6,7], 7)
