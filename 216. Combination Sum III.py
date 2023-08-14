# Backtracking
# Time: O((9！k)/(9-k)!)
# Space: O(k)
# 2023.08.03: yes
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        results = []
        cur = []
        start = 1
        self.backtracking(k, n, cur, results, start)
        return results

    def backtracking(self, k, n, cur, results, start):
        if n == 0 and k == 0:
            results.append(cur[:])
        elif n < 0:
            return
        elif k == 0:
            return
        for i in range(start,10):
            if cur == [] or i > cur[-1]:
                cur.append(i)
                self.backtracking(k-1, n-i, cur, results, start+1)
                cur.pop()

# Backtracking
# Time: O((9！k)/(9-k)!)
# Space: O(k)
# 2023.08.03: yes
# notes: 简化版本，不需要每次从0开始遍历，从后面开始即可
class Solution2:
    def combinationSum3(self, k, n):
        results = []
        def backtrack(remain, comb, next_start):
            if remain == 0 and len(comb) == k:
                # make a copy of current combination
                # Otherwise the combination would be reverted in other branch of backtracking.
                results.append(list(comb))
                return
            elif remain < 0 or len(comb) == k:
                # exceed the scope, no need to explore further.
                return

            # Iterate through the reduced list of candidates.
            for i in range(next_start, 9):
                comb.append(i+1)
                backtrack(remain-i-1, comb, i+1)
                # backtrack the current choice
                comb.pop()

        backtrack(n, [], 0)

        return results

test = Solution()
test.combinationSum3(3,7)
test.combinationSum3(3,9)
test.combinationSum3(4,1)