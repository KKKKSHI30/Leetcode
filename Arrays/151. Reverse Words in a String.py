class Solution:
    # similar way as mine
    def reverseWords(self, s):
        return " ".join(reversed(s.split()))


from collections import deque
# very smart way
class Solution2:
    def reverseWords(self, s):
        left, right = 0, len(s) - 1
        # remove leading spaces
        while left <= right and s[left] == ' ':
            left += 1

        # remove trailing spaces
        while left <= right and s[right] == ' ':
            right -= 1

        d, word = deque(), []
        # push word by word in front of deque
        while left <= right:
            if s[left] == ' ' and word:
                d.appendleft(''.join(word))
                word = []
            elif s[left] != ' ':
                word.append(s[left])
            left += 1
        d.appendleft(''.join(word))

        return ' '.join(d)


class Solution3:
    def trim_spaces(self, s):
        left, right = 0, len(s) - 1
        while left <= right and s[left] == ' ':
            left += 1
        while left <= right and s[right] == ' ':
            right -= 1

        output = []
        while left <= right:
            if s[left] != ' ':
                output.append(s[left])
            elif output[-1] != ' ':
                output.append(s[left])
            left += 1
        return output

    def reverse(self, l, left, right):
        while left < right:
            l[left], l[right] = l[right], l[left]
            left, right = left + 1, right - 1

    def reverse_each_word(self, l):
        n = len(l)
        start = end = 0
        while start < n:
            while end < n and l[end] != ' ':
                end += 1
            self.reverse(l, start, end - 1)
            start = end + 1
            end += 1

    def reverseWords(self, s):
        l = self.trim_spaces(s)
        self.reverse(l, 0, len(l) - 1)
        self.reverse_each_word(l)
        return ''.join(l)


test = Solution3()
test.reverseWords("  hello world  ")