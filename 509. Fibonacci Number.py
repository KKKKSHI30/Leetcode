# Recursion
# Time: O(2^n)
# Space: O(n)
# 2023.06.20: yes
class Solution:
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        return self.fib(N - 1) + self.fib(N - 2)


# Recursion
# Time: O(n)
# Space: O(n)
# 2023.06.20: yes
class Solution2:
    def fib(self, N):
        if N <= 1:
            return N

        cache = [0] * (N + 1)
        cache[1] = 1
        for i in range(2, N + 1):
            cache[i] = cache[i - 1] + cache[i - 2]
        return cache[N]

# Matrix Exponentiation
# Time: O(logn)
# Space: O(logn)
# 2023.06.20: no
class Solution3:
    def fib(self, N):
        if (N <= 1):
            return N
        current = 0
        prev1 = 1
        prev2 = 0
        for i in range(2, N + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
        return current

# Matrix Exponentiation
# Time: O(n)
# Space: O(n)
# 2023.06.20: no
# notes: 纯数，跳过先
class Solution4:
    def fib(self, N):
        if (N <= 1):
            return N

        A = [[1, 1], [1, 0]]
        self.matrix_power(A, N - 1)

        return A[0][0]

    def matrix_power(self, A, N):
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


# Math
# Time: O(logn)
# Space: O(1)
# 2023.06.20: no
# notes: Binet's formula去计算，纯数跳过
class Solution5:
    def fib(self, N: int) -> int:
        golden_ratio = (1 + (5 ** 0.5)) / 2
        return int(round((golden_ratio ** N) / (5 ** 0.5)))














