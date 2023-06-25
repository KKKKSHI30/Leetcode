# Categorize by Count (best approach)
# Time: O(nk)
# Space: O(nk)
# 2023.06.23: yes
import collections

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        results = {}
        for s in strs:
            new_array = [0] * 26
            for i in s:
                new_array[ord(i) - ord('a')] += 1
            if tuple(new_array) not in results:
                results[tuple(new_array)] = [s]
            else:
                results[tuple(new_array)].append(s)
        return results.values()


# Categorize by Sorted String Approach
# Time: O(nk)
# Space: O(nk)
# 2023.06.23: yes
class Solution2(object):
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()

# Tests:
test = Solution()
test.groupAnagrams(["eat","tea","tan","ate","nat","bat"])