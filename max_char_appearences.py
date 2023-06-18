def max_char_appearences(lstOfNum):
    bucket = [[] for i in range(10)]
    for i in lstOfNum:
        bucket[hash(i) % 10].append(i)
    print(f"bucket is {bucket}")
    max_num_appearences = 0
    for i in range(10):
        df = {}
        for j in bucket[i]:
            if j in df:
                df[j] += 1
            else:
                df[j] = 1
        if df != {}:
            max_num_appearences = max(max_num_appearences,max(df.values()))
        continue
    return max_num_appearences



lstOfNum = ["s","a","e","f","e","a","q","e","a","e","r","a","e"]
max_char_appearences(lstOfNum)
