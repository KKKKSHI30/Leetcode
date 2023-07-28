# Bottom Up Dynamic Programming
# Time: O(TP)
# Space: O(TP)
# 2023.07.27: no
# notes: aa可以匹配a*b*c*，因为bc的数量可以为0，这一行ans = dp(i, j+2) or first_match and dp(i+1, j)，考虑到了
# 如果当前字符是不匹配但是有*的情况，注意
class Solution(object):
    def isMatch(self, text, pattern):
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(pattern):
                    ans = i == len(text)
                else:
                    first_match = i < len(text) and pattern[j] in {text[i], '.'}
                    if j+1 < len(pattern) and pattern[j+1] == '*':
                        ans = dp(i, j+2) or first_match and dp(i+1, j)
                    else:
                        ans = first_match and dp(i+1, j+1)
                memo[i, j] = ans
            return memo[i, j]
        return dp(0, 0)

# Top Down Dynamic Programming
# Time: O(TP)
# Space: O(TP)
# 2023.07.27: no
# notes: and has higher precedence than or，其次，思路和前一个方法一样
# 发现了一点新东西： dp的base case就是dp递归到最后的base case，其实根本不需要多想
# 所以逆推的时候就跟递归是一样的，如果是正着推，思路会有点不一样，而且也不一定推的出来
class Solution2(object):
    def isMatch(self, text, pattern):
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]
        dp[-1][-1] = True
        for i in range(len(text), -1, -1):
            for j in range(len(pattern) - 1, -1, -1):
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                if j+1 < len(pattern) and pattern[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]
        return dp[0][0]



# Recursion (exceed time limit)
# Time: O((T+P)^(2^(T+P/2)))
# Space: O(T^2+P^2)
# 2023.07.27: no
# notes: recursion每次需要确认第一个字符match不match，match的话，再考虑剩下的pattern
# 如果是*的话，要不就是匹配两个字符后的pattern，要不就是继续匹配当前字符
class Solution3(object):
    def isMatch(self, text, pattern):
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])

# Tests:
test = Solution2()
test.isMatch("aa","a*b*c*")


