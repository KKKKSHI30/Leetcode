# Two Pointer Algorithm (best approach)
# Time: O(n)
# Space: O(1)
# 2023.06.24: yes
class Solution(object):
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if left < right and s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

# Tests:
s = "A man, a plan, a canal: Panama"
test = Solution()
test.isPalindrome(s)
