def betterCompression(s):
    if s == "":
        return
    cur_num = 0
    cur_alpha = s[0]
    saving = {}
    for i, in s[1:]:
        if ord(i) <= 57 and ord(i) >= 48:
            cur_num = cur_num*10 + int(i)
        else:
            if cur_alpha not in saving:
                saving[cur_alpha] = cur_num
            else:
                saving[cur_alpha] += cur_num
            cur_alpha = i
            cur_num = 0
    if cur_alpha not in saving:
        saving[cur_alpha] = cur_num
    else:
        saving[cur_alpha] += cur_num
    sorted_saving = sorted(saving.items(), key=lambda item: item[0])
    results = ""
    for element in sorted_saving:
        results += element[0]+ str(element[1])
    return results

betterCompression("a12b56c1")
betterCompression("a3c9b2c1")