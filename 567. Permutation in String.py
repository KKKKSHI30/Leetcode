from collections import Counter

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if not s1 or not s2:
            return False
        total_needs = Counter(s1)
        window = {}
        left, right, valid, require = 0, 0, 0, len(total_needs)
        while right < len(s2):
            c = s2[right]
            right += 1
            if c in total_needs:
                window[c] = window.get(c, 0) + 1
                if total_needs[c] == window[c]:
                    valid += 1
            while right - left >= len(s1):
                if valid == require:
                    return True
                d = s2[left]
                left += 1
                if d in total_needs:
                    if window[d] == total_needs[d]:
                        valid -= 1
                    window[d] = window.get(d, 0) - 1
        return False


test = Solution()
test.checkInclusion(s1="ab", s2="eidboaoo")
test.checkInclusion(s1="ab", s2="eidbaooo")


