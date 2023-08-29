def backspaceStringCompare(s1,s2):
    def check(s):
        result = []
        for i in s:
            if i == "#":
                result.pop()
            else:
                result.append(i)
    return check(s1) == check(s2)

backspaceStringCompare('axx#bb#c', 'axbd#c#c')
