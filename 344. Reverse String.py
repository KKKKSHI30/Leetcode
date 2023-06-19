# Two Pointers Approach (best approach)
# Time: O(n)
# Space: O(1)
# 2023.06.18: yes

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        lp, rp = 0, len(s)-1
        while lp < rp:
            s[lp], s[rp] = s[rp], s[lp]
            lp+= 1
            rp -=1
        return

# Recursion Approach:
# Time: O(n)
# Space: O(n)
# 2023.06.18: yes
# notes:只是提供一个方法，但是其实不符合题目要求，真的把脱裤子放屁做到了极致
class Solution2:
    def reverseString(self, s):
        def helper(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                helper(left + 1, right - 1)
        helper(0, len(s) - 1)


# Tests:
test = Solution()
test.reverseString(['a','b','c'])
test.reverseString([])
test.reverseString(['a','b'])