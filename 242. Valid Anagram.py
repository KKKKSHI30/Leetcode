# Frequency Counter Approach
# Time: O(n)
# Space: O(1)
# 2023.06.23: yes
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dic = {}
        for c in s:
            s_dic[c] = s_dic.get(c,0) +1
        for d in t:
            if d in s_dic:
                s_dic[d] -= 1
            else:
                return False
        return all(value == 0 for value in s_dic.values())

# Sorting Approach
# Time: O(nlogn)
# Space: O(1)
# 2023.06.23: yes
class Solution2(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        str1 = sorted(s)
        str2 = sorted(t)
        return str1 == str2


# Tests:
test = Solution()
test.isAnagram("cbba", "bacb")
test.isAnagram(s = "anagram", t = "nagaram")
test.isAnagram(s = "rat", t = "car")