# Ke Shi on July 31th, 2022

def lowest_string(lst_of_str):
    if lst_of_str == None or len(lst_of_str) == 0:
        return ""
    lst_of_str = sorted(lst_of_str)
    res = ""
    # lst_of_str = sorted(lst_of_str)
    for i in range(len(lst_of_str)-1):
        if res + lst_of_str[i] > lst_of_str[i] + res:
            res = lst_of_str[i] + res
        else:
            res = res + lst_of_str[i]
    return res



initial_list = ['a', 'b', 'ab', 'aa', 'ba', 'c', 'ca', 'ac', 'cc']
result = lowest_string(initial_list)