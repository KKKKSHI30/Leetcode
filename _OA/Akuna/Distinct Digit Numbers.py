def repeated_digit(n):
    a = []
    while n != 0:
        d = n % 10
        if d in a:
            return 0
        a.append(d)
        n = n // 10
    return 1

def printUnique(l, r):
    count = 0
    for i in range(l, r + 1):
        s = list(str(i))
        unitDigits = set()
        for j in range(len(s)):
            unitDigits.add(s[j])
        if len(s) == len(unitDigits):
            count += 1
    print(count)


def countNumbers(arr):
    for i in arr:
        printUnique(i[0], i[1])


countNumbers([[7,8],[52,80], [34,84]])
