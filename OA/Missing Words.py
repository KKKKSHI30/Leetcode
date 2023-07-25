# Given two strings, one is a subsequence of all the elements of the first string that occurs
# in the same order within the second string. They don't have to be contiguous in the second string
# but the order must be maintained.  For example, given the string "I like cheese" the word
# ("I" and "cheese") are one possible subsequence of that string. Words are space delimited. Given two strings S and
# T where t is a subsequence of S, report the words of s, missing in T(case Sensitive), in the order, they are missing.
def missingWords(s, t):
    string = s.split(" ")
    sub = t.split(" ")
    result = []
    left = 0

    for i in range(len(string)):
        if len(sub) == left:
            result.append(string[i])
        elif string[i] != sub[left]:
            result.append(string[i])
        else:
            left += 1
    return result

# Example usage:
s = "I am using Python programming language"
t = "am Python language"
print(missingWords(s, t))
