# Greedy - Solving with Stack (best approach)
# Time: O(n)
# Space: O(1)
# 2023.06.22: no
# 1. 通过栈保持顺序一致，且只有一个（判断栈里有没有）2.配合count确保之后还会再出现的字符才会被pop掉
class Solution:
    def removeDuplicateLetters(self,s):
        stk = []  # Stack to store the result after removing duplicates

        # 维护一个计数器记录字符串中字符的数量
        # 因为输入为 ASCII 字符，大小 256 够用了
        count = [0] * 256
        for c in s:
            count[ord(c)] += 1

        inStack = [False] * 256
        for c in s:
            # 每遍历过一个字符，都将对应的计数减一
            count[ord(c)] -= 1

            if inStack[ord(c)]:
                continue

            while stk and stk[-1] > c:
                # 若之后不存在栈顶元素了，则停止 pop
                if count[ord(stk[-1])] == 0:
                    break
                # 若之后还有，则可以 pop
                inStack[ord(stk.pop())] = False

            stk.append(c)
            inStack[ord(c)] = True

        sb = []
        while stk:
            sb.append(stk.pop())

        # 栈中元素插入顺序是反的，需要 reverse 一下
        return ''.join(sb[::-1])


# Greedy - Solving Letter by Letter
# Time: O(n)
# Space: O(n)
# 2023.06.22: no
# notes: 很复杂，递归+greedy，没看懂
from collections import Counter

class Solution2:
    def removeDuplicateLetters(self, s: str) -> str:

        # find pos - the index of the leftmost letter in our solution
        # we create a counter and end the iteration once the suffix doesn't have each unique character
        # pos will be the index of the smallest character we encounter before the iteration ends
        c = Counter(s)
        pos = 0
        for i in range(len(s)):
            if s[i] < s[pos]:
                pos = i
            c[s[i]] -=1
            if c[s[i]] == 0:
                break
        # our answer is the leftmost letter plus the recursive call on the remainder of the string
        # note we have to get rid of further occurrences of s[pos] to ensure that there are no duplicates
        return s[pos] + self.removeDuplicateLetters(s[pos:].replace(s[pos], "")) if s else ''

# Tests:
test = Solution2()
test.removeDuplicateLetters("bcabc")