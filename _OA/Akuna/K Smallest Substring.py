def getSubstring(input_str, k):
    left, right = 0, 0
    ind = 0
    substr = []
    while left <= right and right < len(input_str):
        if input_str[right] == "1":
            ind += 1
        else:
            right += 1
            continue
        if ind == k:
            substr.append(input_str[left:right +1])
            if input_str[left] == '1':
                ind -= 1
            left += 1
            if input_str[right] == '1':
                ind -= 1
            continue
        right += 1
    min_str = ""
    min_lex = float('inf')
    for sub in substr:
        if getRanks(sub) < min_lex:
            min_str = sub
            min_lex = getRanks(sub)
    return min_str

def getRanks(string):
    return pow(2, len(string)) + int(string) -1