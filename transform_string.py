# Ke Shi on Aug 9th, 2022

def transform_string(string):
    if string == None or len(string) == 0:
        return string
    else:
        return process(string, 0)

def process(string, i):
    if i == len(string):
        return 1
    if (string[i] == '0'):
        return 0
    if (string[i] == '1'):
        res = process(string, i+1)
        if i+1 < len(string):
            res += process(string, i+2)
        return res
    if (string[i] == '2'):
        res = process(string, i+1)
        if (i+1 < len(string) and (string[i+1] <= '6' and string[i+1] >= '0')):
            res = process(string, i+2)
        return res
    return process(string, i+1)


test1 = "112341231211"
result = transform_string(test1)