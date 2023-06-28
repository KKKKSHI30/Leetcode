#  Approach
# Time: O(m)
# Space: O(k)
# 2023.06.26: yes
from collections import Counter


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        counts = Counter(magazine)
        for i in range(len(ransomNote)):
            if ransomNote[i] in counts:
                counts[ransomNote[i]] -= 1
                if counts[ransomNote[i]] < 0:
                    return False
            else:
                return False
        return True


# Simulation Approach
# Time: O(m)
# Space: O(k)
# 2023.06.26: yes
class Solution2(object):
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # For each character, c,  in the ransom note.
        for c in ransomNote:
            # If there are none of c left in the String, return False.
            if c not in magazine:
                return False
            # Find the index of the first occurrence of c in the magazine.
            location = magazine.index(c)
            # Use splicing to make a new string with the characters
            # before "location" (but not including), and the characters
            # after "location".
            magazine = magazine[:location] + magazine[location + 1:]
        # If we got this far, we can successfully build the note.
        return True

# Two HashMaps Approach
# Time: O(m)
# Space: O(k)
# 2023.06.26: yes
class Solution3(object):
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        # Check for obvious fail case.
        if len(ransomNote) > len(magazine): return False

        # In Python, we can use the Counter class. It does all the work that the
        # makeCountsMap(...) function in our pseudocode did!
        magazine_counts = Counter(magazine)
        ransom_note_counts = Counter(ransomNote)

        # For each *unique* character in the ransom note:
        for char, count in ransom_note_counts.items():
            # Check that the count of char in the magazine is equal
            # or higher than the count in the ransom note.
            magazine_count = magazine_counts[char]
            if magazine_count < count:
                return False

        # If we got this far, we can successfully build the note.
        return True

# Sorting and Stacks Approach
# Time: O(mlogm)
# Space: O(m)
# 2023.06.26: yes
class Solution4(object):
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        # Check for obvious fail case.
        if len(ransomNote) > len(magazine): return False

        # Reverse sort the note and magazine. In Python, we simply
        # treat a list as a stack.
        ransomNote = sorted(ransomNote, reverse=True)
        magazine = sorted(magazine, reverse=True)

        # While there are letters left on both stacks:
        while ransomNote and magazine:
            # If the tops are the same, pop both because we have found a match.
            if ransomNote[-1] == magazine[-1]:
                ransomNote.pop()
                magazine.pop()
            # If magazine's top is earlier in the alphabet, we should remove that
            # character of magazine as we definitely won't need that letter.
            elif magazine[-1] < ransomNote[-1]:
                magazine.pop()
            # Otherwise, it's impossible for top of ransomNote to be in magazine.
            else:
                return False
                # Return true iff the entire ransomNote was built.
        return not ransomNote




# Tests:
test = Solution()
test.canConstruct(ransomNote = "a", magazine = "b")
test.canConstruct(ransomNote = "aa", magazine = "ab")
test.canConstruct(ransomNote = "aa", magazine = "aab")