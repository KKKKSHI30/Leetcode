# Given a string of words separated by spaces. The task is to find the first maximum length even word from the string.
# Eg: “You are given an array of n numbers” The answer would be “an” and not “of” because “an” comes before “of”.
def evenMaximumString(s):
    result = ""
    max_len = 0
    s = s.split()
    for i in s:
        cur_len = len(i)
        if cur_len % 2 == 0:
            if cur_len > max_len:
                result = i
            elif cur_len == max_len:
                if i < result:
                    result = i
    return result




# Tests:
evenMaximumString("this is a test string")
evenMaximumString("geeksforgeeks is a platform for geeks")