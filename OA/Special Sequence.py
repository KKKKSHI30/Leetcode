# same as lc 38
class Solution:
    def getSequence(self, n):
        if n == 1:
            return "1"
        prev = self.getSequence(n-1)
        res = ''
        cnt = 1

        for i in range(len(prev)):
            if (i == len(prev)-1) or (prev[i] != prev[i+1]):
                res += (str(cnt) + prev[i])
                # res.append([cnt, prev[i]])
                cnt =1
            else:
                cnt += 1
        return res

    def getSum(self, n):
        res = 0
        seq = self.getSequence(n)
        for s in seq:
            res += int(s)
        return res

# Tests:
test = Solution()
test.getSequence(4)