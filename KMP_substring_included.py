# KMP 算法
def getNextArray(lstOfChar):
    nextarray = []
    if len(lstOfChar) == -1:
        return nextarray.append(-1)
    nextarray.append(-1)
    nextarray.append(0)
    i = 2   # 数组的位置
    cn = 0  # 哪个字符和i-1位置比
    while i < len(lstOfChar):
        # 如果新加的后面那个字符和cn一样
        if lstOfChar[i-1] == lstOfChar[cn]:
            # nextarray后面加一，i往后一位，cn也可以往后一位了
            nextarray.append(cn+1)
            i += 1
            cn += 1
        # 跳回去
        elif cn > 0:
            cn = nextarray[cn]
        # 找不到了，直接是0
        else:
            i += 1
            nextarray.append(0)
    print(nextarray)
    return nextarray

def substring_included(s1, s2):
    if s1 == None or s2 == None or len(s2) < 1 or len(s1) < len(s2):
        return False
    s1 = list(s1)
    s2 = list(s2)
    i1 = 0
    i2 = 0
    nextArray = getNextArray(s2)
    while (i1 < len(s1) and i2 < len(s2)):
        if s1[i1] == s2[i2]:
            i1 += 1
            i2 += 1
        # str2就算回到开头也不行了
        elif nextArray[i2] == -1:
            i1 += 1
        # 跳到str2中间
        else:
            i2 = nextArray[i2]
    if i2 == len(s2):
        return True  # i1 - i2
    else:
        return False

substring_included("abcd", "abc")



