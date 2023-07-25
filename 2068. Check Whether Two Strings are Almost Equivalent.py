from collections import Counter

class Solution(object):
    def checkAlmostEquivalent(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        return all(v < 4 for v in ((Counter(word1) - Counter(word2)) + (Counter(word2) - Counter(word1))).values())