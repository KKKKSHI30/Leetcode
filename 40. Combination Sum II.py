from collections import Counter

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        results = []
        cur = []
        candidates = sorted(candidates)
        self.backtracking(candidates, cur, target, results, 0)
        return results

    def backtracking(self, candidates, cur, target, results, start):
        if target == 0:
            results.append(cur[:])
            return
        elif target < 0:
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i-1]:
                continue
            cur.append(candidates[i])
            self.backtracking(candidates, cur, target - candidates[i], results, i+1)
            cur.pop()

test = Solution()
test.combinationSum2([10,1,2,7,6,1,5], 8)


class Solution2:
    def combinationSum2(self, candidates, target):

        def backtrack(comb, remain, curr, counter, results):
            if remain == 0:
                results.append(list(comb))
                return
            elif remain < 0:
                return

            for next_curr in range(curr, len(counter)):
                candidate, freq = counter[next_curr]

                if freq <= 0:
                    continue

                # add a new element to the current combination
                comb.append(candidate)
                counter[next_curr] = (candidate, freq-1)

                # continue the exploration with the updated combination
                backtrack(comb, remain - candidate, next_curr, counter, results)

                # backtrack the changes, so that we can try another candidate
                counter[next_curr] = (candidate, freq)
                comb.pop()

        results = []
        counter = Counter(candidates)
        counter = [(c, counter[c]) for c in counter]
        backtrack(comb = [], remain = target, curr = 0, counter = counter, results = results)
        return results

test = Solution2()
test.combinationSum2([10,1,2,7,6,1,5], 8)

