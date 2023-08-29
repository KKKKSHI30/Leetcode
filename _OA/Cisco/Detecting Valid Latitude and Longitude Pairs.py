# 题目：https://www.hackerrank.com/challenges/detecting-valid-latitude-and-longitude/problem
import re
for _ in range(int(input())):
    string = re.search('(.*)', input()).group()
    if string:
        string = re.sub("[(|)|+|\-| ]","", string)
        n1, n2 = string.split(',')
        if n1[0] == '0' or n2[0] == '0' or n1[-1] == '.' or n2[-1] == '.':
            print("Invalid")
        else:
            n1, n2 = float(n1), float(n2)
            if n1 >= -90 and n1 <= 90 and n2 >= -180 and n2 <= 180:
                print("Valid")
            else:
                print("Invalid")
    else:
        print("Invalid")
