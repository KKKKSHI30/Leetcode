class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        saving = {}
        paragraph = paragraph.replace(' ', ',').split(',')
        for i, n in enumerate(paragraph):
            n = n.strip().lower()
            n = n.replace(",","")
            n = n.replace(".","")
            n = n.replace("!","")
            n = n.replace("?","")
            n = n.replace(";", "")
            n = n.replace("'", "")
            n = n.replace("...", "")
            if n == "":
                continue
            if n in saving:
                saving[n] += 1
            else:
                saving[n] = 1
        # saving = {k: v for k, v in sorted(saving.items(), key=lambda item: item[1], reverse = True)}
        saving = sorted(saving, key=saving.get, reverse=True)
        for i,n in enumerate(saving):
            if n in banned:
                continue
            else:
                return n

def check(test):
    a = ""
    for c in test:
        if c.isalnum():
            c = c.lower()
        else:
            c = " "
        a += c
    return a

# tips: when figure out a string, it is not necessary to divide the string,
# we can also using char to dealing, it is easier to check the punctuation or other stuff
class Solution2(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        # see check(test) function for details
        lowerstr = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])

        words = lowerstr.split()
        wordfreq = {}
        mostfreq = 0
        mostfreqword = ""
        bannedwords = set(banned)

        for word in words:
            if word not in bannedwords:
                if word not in wordfreq:
                    wordfreq[word] = 0
                wordfreq[word] += 1

        for word, freq in wordfreq.items():
            if freq > mostfreq:
                mostfreq = freq
                mostfreqword = word

        return mostfreqword


class Solution3(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        punc = {' ', ',', '!', '?', "'", ';', '.'}
        bannedSet = set()
        for word in banned:
            bannedSet.add(word.lower())

        words = []
        currentWord = ""
        for i in range(len(paragraph)):
            c = paragraph[i]
            if c in punc:
                if currentWord == "":
                    continue
                else:
                    words.append(currentWord)
                    currentWord = ""
            else:
                currentWord += c.lower()
        if currentWord != "":
            words.append(currentWord)

        frequency = {}
        maxFreq = 0
        mostFrequent = ""
        for word in words:
            if word not in frequency:
                if word in bannedSet:
                    frequency[word] = -1
                else:
                    frequency[word] = 1
            elif frequency[word] != -1:
                frequency[word] += 1
            if frequency[word] > maxFreq:
                maxFreq = frequency[word]
                mostFrequent = word
        return mostFrequent

test = Solution()
# test.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", "hit")
# test.mostCommonWord("a.", "")
# test.mostCommonWord("a, a, a, a, b,b,b,c, c", "a")
test.mostCommonWord("Bob. hIt, baLl", ["bob", "hit"])