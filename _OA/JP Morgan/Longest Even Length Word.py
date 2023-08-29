def longestEvenWord(sentence):
    sentence = sentence.split(" ")
    res = ""
    for s in sentence:
        if len(s) > len(res):
            res = s
    return res

longestEvenWord("It is a pleasant day today")