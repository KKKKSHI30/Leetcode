def entryTime(s, keypad):
    def isAdjacent(prev, cur):
        pr, pc = keypad9[prev]
        cr, cc = keypad9[cur]
        if abs(pr-cr) <= 1 and abs(pc-cc) <= 1:
            return True
        return False

    keypad9 = {}
    for i in range(0, len(keypad)):
        keypad9[keypad[i]] = (i // 3, i % 3)
    res = 0
    for i in range(0, len(s)):
        if i != 0:
            prev = s[i - 1]
            cur = s[i]
            if isAdjacent(prev, cur):
                res += 1
            else:
                res += 2
    return res

# Tests:
# 9 2 3
# 8 5 7
# 6 1 4
keypad = "923857614"
s = "423692"
entryTime(s, keypad)

