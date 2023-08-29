def threhold(numCalls, alertThreshold, precedingMinutes):
    result = 0
    not_exceed = alertThreshold*precedingMinutes
    cur_total_value = 0
    cur_block = []
    for i in numCalls:
        if len(cur_block) < precedingMinutes:
            cur_block.append(i)
            cur_total_value += i
        else:
            if cur_total_value > not_exceed:
                result += 1
            tmp = cur_block.pop(0)
            cur_total_value -= tmp
            cur_block.append(i)
            cur_total_value += i
    if cur_total_value > not_exceed:
        result += 1
    return result

threhold([2,2,2,2,5,5,5,8], 4, 3)
