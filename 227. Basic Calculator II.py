# Using Stack
# Time: O(n)
# Space: O(n)
# 2023.07.22: yes
import itertools
from math import trunc
class Solution:
    def calculate(self, s):
        if not s:
            return "0"
        stack, num, sign = [], 0, "+"
        for i in range(len(s)):
            if s[i].isdigit():
                num = num*10+ord(s[i])-ord("0")
            if (not s[i].isdigit() and not s[i].isspace()) or i == len(s)-1:
                if sign == "-":
                    stack.append(-num)
                elif sign == "+":
                    stack.append(num)
                elif sign == "*":
                    stack.append(stack.pop()*num)
                else:
                    tmp = stack.pop()
                    if tmp//num < 0 and tmp%num != 0:
                        stack.append(tmp//num+1)
                    else:
                        stack.append(tmp//num)
                sign = s[i]
                num = 0
        return sum(stack)

# Optimised Approach without the stack
# Time: O(n)
# Space: O(1)
# 2023.07.22: yes
class Solution2:
    def calculate(self, s: str) -> int:
        pending_res = res = num = 0
        pending_op = "+"

        for char in itertools.chain(s, '+'):
            if char.isdigit():
                num = 10 * num + int(char)

            elif char in {'+', '-', '*', '/'}:
                if pending_op == '+':
                    pending_res += num
                elif pending_op == '-':
                    pending_res -= num
                elif pending_op == '*':
                    pending_res *= num
                else:
                    pending_res = int(pending_res / num)

                if char in {'+', '-'}:
                    res += pending_res
                    pending_res = 0

                pending_op = char
                num = 0

        return res
# Tests:
test = Solution2()
test.calculate("3 +2*2")