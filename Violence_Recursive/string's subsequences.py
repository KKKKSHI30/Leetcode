# Ke Shi on Aug 7th, 2022
import copy

def subsequences(s):
    s = list(s)
    process(s, 0, [])

def process(s, i, res):
    if (i == len(s)):
        print(''.join(res))
        return
    res_keep = copy.deepcopy(res)
    res_keep.append(s[i])
    process(s, i+1, res_keep)
    res_no_include = copy.deepcopy(res)
    process(s, i+1, res_no_include)

def subsequences2(s):
    s = list(s)
    process2(s, 0)

def process2(s, i):
    if (i == len(s)):
        print(''.join(s))
        return
    process2(s, i+1)
    tmp = s.pop(i)
    s.insert(i, "")
    process2(s, i+1)
    s.pop(i)
    s.insert(i, tmp)

# subsequences("abc")
subsequences2("abc")


