# Sliding Window
# Time: O(nm)
# Space: O(1)
# 2023.06.21: yes
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        m = len(needle)
        n = len(haystack)

        for window_start in range(n - m + 1):
            for i in range(m):
                if needle[i] != haystack[window_start + i]:
                    break
                if i == m - 1:
                    return window_start

        return -1


# Rabin-Karp Approach
# Time: O(n)，只有python3是O(n)，因为可以处理大数字，其他语言考虑double hash Rabin-Karp
# Space: O(1)
# 2023.06.21: yes
class Solution2:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        h = len(haystack)
        needle_hash = 0
        window_hash = 0
        if h < n:
            return -1
        RADIX = 26
        RL = RADIX ** (n - 1)
        # add a number at the end
        for i in range(n):
            appendval = ord(needle[i]) - ord('a')
            needle_hash = needle_hash * RADIX + appendval
        left, right = 0, 0
        while right < h:
            window_hash = RADIX * window_hash + (ord(haystack[right]) - ord('a'))
            right += 1
            if right - left == n:
                if window_hash == needle_hash:
                    return left
                window_hash -=(ord(haystack[left]) - ord('a')) * RL
                left += 1
        return -1

test = Solution2()
test.strStr(haystack = "sadbutsad", needle = "sad")
test.strStr(haystack = "leetcode", needle = "leeto")
test.strStr(haystack = "leetcodee", needle = 'tco')

# Rabin-Karp Approach
# Time: O(nm)
# Space: O(1)
# 2023.06.21: no
# notes: 本质就是两个hash，然后看一不一样，因为一个hash之后mod是有可能一样的，两个hash基本不可能了
class Solution3:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(needle)
        n = len(haystack)

        if n < m:
            return -1

        # CONSTANTS
        RADIX_1 = 26
        MOD_1 = 10**9+33
        MAX_WEIGHT_1 = 1
        RADIX_2 = 27
        MOD_2 = 2**31-1
        MAX_WEIGHT_2 = 1

        for _ in range(m):
            MAX_WEIGHT_1 = (MAX_WEIGHT_1 * RADIX_1) % MOD_1
            MAX_WEIGHT_2 = (MAX_WEIGHT_2 * RADIX_2) % MOD_2

        # Function to compute hash_pair of m-String
        def hash_pair(string):
            hash_1 = hash_2 = 0
            factor_1 = factor_2 = 1
            for i in range(m - 1, -1, -1):
                hash_1 += ((ord(string[i]) - 97) * (factor_1)) % MOD_1
                factor_1 = (factor_1 * RADIX_1) % MOD_1
                hash_2 += ((ord(string[i]) - 97) * (factor_2)) % MOD_2
                factor_2 = (factor_2 * RADIX_2) % MOD_2

            return [hash_1 % MOD_1, hash_2 % MOD_2]

        # Compute hash pairs of needle
        hash_needle = hash_pair(needle)

        # Check for each m-substring of haystack, starting at window_start
        for window_start in range(n - m + 1):
            if window_start == 0:
                # Compute hash pairs of the First Substring
                hash_hay = hash_pair(haystack)
            else:
                # Update Hash pairs using Previous using O(1) Value
                hash_hay[0] = (((hash_hay[0] * RADIX_1) % MOD_1
                               - ((ord(haystack[window_start - 1]) - 97)
                                  * (MAX_WEIGHT_1)) % MOD_1
                               + (ord(haystack[window_start + m - 1]) - 97))
                               % MOD_1)
                hash_hay[1] = (((hash_hay[1] * RADIX_2) % MOD_2
                               - ((ord(haystack[window_start - 1]) - 97)
                                  * (MAX_WEIGHT_2)) % MOD_2
                               + (ord(haystack[window_start + m - 1]) - 97))
                               % MOD_2)

            # If the hash matches, return immediately.
            # Probability of Spurious Hit tends to zero
            if hash_needle == hash_hay:
                return window_start
        return -1

# Knuth–Morris–Pratt Algorithm Approach
# Time: O(n)
# Space: O(m)
# 2023.06.21: no
class Solution4:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(needle)
        n = len(haystack)

        if n < m:
            return -1

        # PREPROCESSING
        # longest border array
        longest_border = [0] * m
        # Length of Longest Border for prefix before it.
        prev = 0
        # Iterating from index-1. longest_border[0] will always be 0
        i = 1

        while i < m:
            if needle[i] == needle[prev]:
                # Length of Longest Border Increased
                prev += 1
                longest_border[i] = prev
                i += 1
            else:
                # Only empty border exist
                if prev == 0:
                    longest_border[i] = 0
                    i += 1
                # Try finding longest border for this i with reduced prev
                else:
                    prev = longest_border[prev - 1]

        # SEARCHING
        # Pointer for haystack
        haystack_pointer = 0
        # Pointer for needle.
        # Also indicates number of characters matched in current window.
        needle_pointer = 0

        while haystack_pointer < n:
            if haystack[haystack_pointer] == needle[needle_pointer]:
                # Matched Increment Both
                needle_pointer += 1
                haystack_pointer += 1
                # All characters matched
                if needle_pointer == m:
                    # m characters behind last matching will be window start
                    return haystack_pointer - m
            else:
                if needle_pointer == 0:
                    # Zero Matched
                    haystack_pointer += 1
                else:
                    # Optimally shift left needle_pointer.
                    # Don't change haystack_pointer
                    needle_pointer = longest_border[needle_pointer - 1]

        return -1