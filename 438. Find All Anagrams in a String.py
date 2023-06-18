from collections import Counter

class Solution:
    def findAnagrams(self, s, p):
        if not s or not p:
            return []
        results = []
        total_needs = Counter(p)
        window = {}
        left, right, valid, require = 0, 0, 0, len(total_needs)
        while right < len(s):
            c = s[right]
            right += 1
            if c in total_needs:
                window[c] = window.get(c, 0) + 1
                if total_needs[c] == window[c]:
                    valid += 1
            while right - left >= len(p):
                if valid == require:
                    results.append(left)
                d = s[left]
                left += 1
                if d in total_needs:
                    if window[d] == total_needs[d]:
                        valid -= 1
                    window[d] = window.get(d, 0)-1
        return results

test = Solution()
test.findAnagrams(s = "cbaebabacd", p = "abc")
test.findAnagrams(s = "abab", p = "ab")


class Solution2:
    def findAnagrams(self, s: str, p: str):
        ns, np = len(s), len(p)
        if ns < np:
            return []
        p_count, s_count = [0] * 26, [0] * 26
        for ch in p:
            p_count[ord(ch) - ord('a')] += 1
        output = []
        for i in range(ns):
            s_count[ord(s[i]) - ord('a')] += 1
            if i >= np:
                s_count[ord(s[i - np]) - ord('a')] -= 1
            if p_count == s_count:
                output.append(i - np + 1)
        return output

test = Solution2()
test.findAnagrams(s = "cbaebabacd", p = "abc")
test.findAnagrams(s = "abab", p = "ab")