# Greedy Approach
# Time: O(n)
# Space: O(1)
# 2023.06.25: yes
from collections import Counter

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        counts = Counter(s)
        total = 0
        odd = False
        for value in counts.values():
            if value % 2 == 0:
                total += value
            else:
                odd = True
                total += ((value//2)*2)
        if odd:
            total += 1
        return total

# Greedy Approach
# Time: O(n)
# Space: O(1)
# 2023.6.25: yes
# notes: 和上面一样，就是简短点，自己写的有点长
class Solution2:
    def longestPalindrome(self, s):
        ans = 0
        for v in Counter(s).itervalues():
            ans += v / 2 * 2
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1
        return ans

# Tests:
test = Solution()
test.longestPalindrome('ccc')
test.longestPalindrome('a')

