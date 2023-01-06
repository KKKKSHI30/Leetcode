class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        results = []
        cur = []
        self.backtracking(n, n, cur, results)
        return results

    def backtracking(self, left, right, cur, results):
        if right < left:
            return
        if left < 0 or right < 0:
            return
        if left == 0 and right == 0:
            results.append("".join(cur))
            return

        cur.append('(')
        self.backtracking(left-1, right, cur, results)
        cur.pop()
        cur.append(')')
        self.backtracking(left, right-1, cur, results)
        cur.pop()

test = Solution()
test.generateParenthesis(3)

class Solution2(object):
    def generateParenthesis(self, n):
        def generate(A = []):
            if len(A) == 2*n:
                if valid(A):
                    ans.append("".join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()

        def valid(A):
            bal = 0
            for c in A:
                if c == '(': bal += 1
                else: bal -= 1
                if bal < 0: return False
            return bal == 0

        ans = []
        generate()
        return ans

class Solution3(object):
    def generateParenthesis(self, N):
        if N == 0: return ['']
        ans = []
        for c in range(N):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(N-1-c):
                    ans.append('({}){}'.format(left, right))
        return ans

test = Solution3()
test.generateParenthesis(2)