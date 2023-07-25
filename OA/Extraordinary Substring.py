def countStrings(input_str):
    num = 0
    numset = []
    for s in input_str:
        numset.append(letter2num(s))
    for i in range(len(numset)):
        j = i
        while j < len(numset):
            if sum(numset[i:j+1]) % (j-i+1) == 0:
                num += 1
            j += 1
    return num

def letter2num(letter):
    return (ord(letter) - ord('a') + 4) //3