def encryptionValidity(instructionCount, validityPeriod, keys):
    max_divisibility = 0
    for i, key in enumerate(keys):
        divisibility = 0
        for j in range(len(keys)):
            if key >= keys[j] and key % keys[j] == 0:
                divisibility += 1
        max_divisibility = max(max_divisibility, divisibility)
    return instructionCount*validityPeriod >= max_divisibility*10000




encryptionValidity(1000, 10000, [2,4,8,2])