# Sliding Window Approach
# Time: O(l1+ (l2-l1)), l1 is length of s1, l2 is length of s2
# Space: O(1)
# 2023.06.20: no
# notes: 重点是s1的排列是不是s2的子串，代表子串长度是固定的，所以检查的条件是固定长度的时候，是不是needs里的东西都符合
from collections import Counter
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        needs, window = Counter(s1), {}
        valid, left, right = 0, 0, 0
        while right < len(s2):
            c = s2[right]
            right += 1
            if c in needs:
                window[c] = window.get(c, 0) + 1
                if window[c] == needs[c]:
                    valid += 1
            while right - left >= len(s1):
                if valid == len(needs):
                    return True
                d = s2[left]
                left += 1
                if d in needs:
                    if window[d] == needs[d]:
                        valid -= 1
                    window[d] -= 1
        return False

# Optimized Sliding Window Approach
# Time: O(l1+ 26*(l2-l1)), l1 is length of s1, l2 is length of s2
# Space: O(1)
# 2023.06.20: no
# notes: 核心观点是把这段长度记录下来和原始的对比，每次右移一次，都会进行更新
class Solution2:
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False

        s1map = [0] * 26
        s2map = [0] * 26

        for i in range(len(s1)):
            s1map[ord(s1[i]) - ord('a')] += 1
            s2map[ord(s2[i]) - ord('a')] += 1

        count = 0
        for i in range(26):
            if s1map[i] == s2map[i]:
                count += 1

        for i in range(len(s2) - len(s1)):
            r = ord(s2[i + len(s1)]) - ord('a')
            l = ord(s2[i]) - ord('a')

            if count == 26:
                return True

            s2map[r] += 1
            if s2map[r] == s1map[r]:
                count += 1
            elif s2map[r] == s1map[r] + 1:
                count -= 1

            s2map[l] -= 1
            if s2map[l] == s1map[l]:
                count += 1
            elif s2map[l] == s1map[l] - 1:
                count -= 1

        return count == 26

# Using sorting Approach
# Time: O(l1*logl1+ l1*logl1*(l2-l1)), l1 is length of s1, l2 is length of s2
# Space: O(l1)
# 2023.06.20: no
# notes: 写起来是真的容易啊，就是效率偏慢，因为转成了array,不过也不失为一种方法
class Solution3:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = self.sort(s1)
        for i in range(len(s2) - len(s1) + 1):
            if s1 == self.sort(s2[i:i + len(s1)]):
                return True
        return False

    def sort(self, s: str) -> str:
        return ''.join(sorted(s))

# Using hashmap Approach
# Time: O(l1*logl1+ l1*logl1*(l2-l1)), l1 is length of s1, l2 is length of s2
# Space: O(l1)
# 2023.06.20: no
class Solution4:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1map = {}
        for char in s1:
            s1map[char] = s1map.get(char, 0) + 1

        for i in range(len(s2) - len(s1) + 1):
            s2map = {}
            for j in range(len(s1)):
                s2map[s2[i + j]] = s2map.get(s2[i + j], 0) + 1
            if self.matches(s1map, s2map):
                return True
        return False

    def matches(self, s1map: dict, s2map: dict) -> bool:
        for key in s1map:
            if s1map[key] - s2map.get(key, -1) != 0:
                return False
        return True

# Using Array Approach
# Time: O(l1+ 26*l1*(l2-l1)), l1 is length of s1, l2 is length of s2
# Space: O(l1)
# 2023.06.20: no
class Solution5:
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False
        s1map = [0] * 26
        for char in s1:
            s1map[ord(char) - ord('a')] += 1
        for i in range(len(s2) - len(s1) + 1):
            s2map = [0] * 26
            for j in range(len(s1)):
                s2map[ord(s2[i + j]) - ord('a')] += 1
            if self.matches(s1map, s2map):
                return True
        return False

    def matches(self, s1map, s2map):
        for i in range(26):
            if s1map[i] != s2map[i]:
                return False
        return True


test = Solution2()
test.checkInclusion(s1="ab", s2="eidboaoo")
test.checkInclusion(s1="ab", s2="eidbaooo")


