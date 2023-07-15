"""
2. Math Lego Block
思路：分别遍历数组AB求sumA, zeros_in_A， sumB， zeros_in_B.
            return max(sumA+zeros_in_A， sumB+zeros_in_B)

如sumA+zeros_in_A比 sumB+zeros_in_B小，但是A中并没有空白格，则-1.
"""
def mathLegoBlock(rowA, rowB):
    sumA, sumB = sum(rowA), sum(rowB)
    zeroA, zeroB = rowA.count(0), rowB.count(0)
    totalA, totalB = sumA + zeroA, sumB + zeroB
    if totalA < totalB and zeroA == 0:
        return -1
    elif totalB < totalA and zeroB == 0:
        return -1
    return max(totalA, totalB)

# Example usage:
min_sum = mathLegoBlock([1,0,2], [1,3,0,0])
min_sum2 = mathLegoBlock([2,5,0,1,1], [2,1,0,0])
min_sum3 = mathLegoBlock([0,0,0], [1,1])


