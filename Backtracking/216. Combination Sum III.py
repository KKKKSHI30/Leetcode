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

test = Solution()
test.combinationSum3(3,7)
test.combinationSum3(3,9)
test.combinationSum3(4,1)