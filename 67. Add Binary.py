# Bit Manipulation
# Time: O(n)
# Space: O(1)
# 2023.08.02: yes
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a, 2) + int(b, 2))[2:]

# Bit-by-Bit Computation
# Time: O(max(M,N))
# Space: O(max(M,N))
# 2023.08.02: no
# notes: 纯一位位加，还是别看了
class Solution2:
    def addBinary(self, a, b) -> str:
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)

        carry = 0
        answer = []
        for i in range(n - 1, -1, -1):
            if a[i] == '1':
                carry += 1
            if b[i] == '1':
                carry += 1

            if carry % 2 == 1:
                answer.append('1')
            else:
                answer.append('0')

            carry //= 2

        if carry == 1:
            answer.append('1')
        answer.reverse()

        return ''.join(answer)

# Bit Manipulation
# Time: O(N+M)
# Space: O(max(M,N))
# 2023.08.02: no
# notes: answer算出当前的位数可以被算到结果的，carry是算出，两个1需要进位的情况，左移就是进位，
# loop的原因是防止多次重复进位，可以都加上去
class Solution3:
    def addBinary(self, a, b) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]


# Tests:
test = Solution3()
test.addBinary("1010", "1011")

# 0001

# 1010  << 1      10100

# 1, 10100
# 10101, 0

