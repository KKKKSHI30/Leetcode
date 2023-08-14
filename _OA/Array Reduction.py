
def reductionCost(num):
    result = 0
    while len(num) > 1:
        ele1 = num.pop(0)
        ele2 = num.pop(0)
        total = ele1 + ele2
        num.append(total)
        result += total
    return result

# test:
reductionCost([4,1,2,3,4])
reductionCost([1,2,3])

