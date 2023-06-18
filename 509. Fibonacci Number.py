class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        saving = [0, 1]
        for i in range(n-1):
            saving.append(saving[i] + saving[i+1])
        return saving[n]

    def fib2(self, n):
        if n == 0:
            return 0
        n0 = 0
        n1 = 1
        for i in range(n-1):
            n2 = n0 + n1
            n0 = n1
            n1 = n2
        return n1

class Solution2:
    # recursion, not good
    # time: O(2^n), space: O(n)
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        return self.fib(N - 1) + self.fib(N - 2)


class Solution3:
    cache = {0: 0, 1: 1}

    def fib(self, N: int) -> int:
        if N in self.cache:
            return self.cache[N]
        self.cache[N] = self.fib(N - 1) + self.fib(N - 2)
        return self.cache[N]

class Solution4:
    def fib(self, N: int) -> int:
        if (N <= 1):
            return N

        A = [[1, 1], [1, 0]]
        self.matrix_power(A, N - 1)

        return A[0][0]

    def matrix_power(self, A, N: int):
        if (N <= 1):
            return A

        self.matrix_power(A, N // 2)
        self.multiply(A, A)
        B = [[1, 1], [1, 0]]

        if (N % 2 != 0):
            self.multiply(A, B)

    def multiply(self, A, B) -> None:
        x = A[0][0] * B[0][0] + A[0][1] * B[1][0]
        y = A[0][0] * B[0][1] + A[0][1] * B[1][1]
        z = A[1][0] * B[0][0] + A[1][1] * B[1][0]
        w = A[1][0] * B[0][1] + A[1][1] * B[1][1]

        A[0][0] = x
        A[0][1] = y
        A[1][0] = z
        A[1][1] = w

# Contributed by LeetCode user mereck.
class Solution5:
    def fib(self, N: int) -> int:
        golden_ratio = (1 + (5 ** 0.5)) / 2
        return int(round((golden_ratio ** N) / (5 ** 0.5)))

test = Solution()
test.fib2(0)