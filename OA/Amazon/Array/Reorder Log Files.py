class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letter = []
        dig = []
        for i, n in enumerate(logs):
            check = n.split()[1]
            if check.isnumeric():
                dig.append(n)
            else:
                letter.append(n)
        letter = sorted(letter, key=lambda x: (x.split()[1:], x.split()[0]))
        return letter + dig


class Solution2(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        def compare(s1, s2):
            # custom comparator for letter logs
            if s1[-1].isnumeric():
                return 1
            if s2[-1].isnumeric():
                return -1
            k1 = s1.index(" ") + 1
            k2 = s2.index(" ") + 1
            l1 = s1[k1:]
            l2 = s2[k2:]
            if l1 < l2:
                return -1
            elif l1 > l2:
                return 1
            elif l1 == l2:
                if s1[0:k1] > s2[0:k2]:
                    return 1
                elif s1[0:k1] < s2[0:k2]:
                    return -1
            return 0
        logs.sort(cmp=compare)
        return logs


test1 = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
test2 = ["let1 art can","let2 own kit dig","let3 art zero"]
test3 = ["dig1 8 1 5 1","dig3 art zero", "dig2 3 6"]
test4 = ["let1 art can","let4 own kit dig", "let2 own kit dig","let3 art zero"]
test5 = ["1 n u", "r 527", "j 893", "6 14", "6 82"]
test = Solution()
test.reorderLogFiles(test1)
test.reorderLogFiles(test4)
test.reorderLogFiles(test5)








