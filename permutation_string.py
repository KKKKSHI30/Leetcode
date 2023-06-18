# Ke Shi on Aug 7th, 2022

def permutation_string(s):
    res = []
    if s == None or len(s) == 0:
        return res
    s = list(s)
    process(s, 0, res)
    return res

def process(s, i, res):
    if i == len(s):
        res.append(''.join(s))
    for j in range(i, len(s)):
        s[i], s[j] = s[j], s[i]
        process(s, i+1, res)
        s[i], s[j] = s[j], s[i]

def permutation_string2(s):
    res = []
    if s == None or len(s) == 0:
        return res
    s = list(s)
    process2(s, 0, res)
    return res

def process2(s, i, res):
    if i == len(s):
        res.append(''.join(s))
    visit = [None] * 26
    for j in range(i, len(s)):
        if (not visit[ord(s[j]) - ord('a')]):
            visit[ord(s[j]) - ord('a')] = True
            s[i], s[j] = s[j], s[i]
            process2(s, i+1, res)
            s[i], s[j] = s[j], s[i]

permutation_string("abc")
permutation_string2("aabb")
