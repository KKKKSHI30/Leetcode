def getMinCost(start, end, costRows, costCols):
    cost_r = sum(costRows[start[0]:end[0]])
    cost_c = sum(costCols[start[1]:end[1]])
    return cost_c + cost_r

def minCost(rows, cols, initR, initC, finalR, finalC, costRows, costCols):
    # Write your code here
    cost = 0
    add = 0

    # initR to finalR
    if initR < finalR:
        add = 1
    else:
        add = -1

    while initR != finalR:
        if add == 1:
            cost += costRows[initR]
            initR += add
        else:
            initR += add
            cost += costRows[initR]

    # initC to finalC
    if initC < finalC:
        add = 1
    else:
        add = -1

    while initC != finalC:
        if add == 1:
            cost += costCols[initC]
            initC += add
        else:
            initC += add
            cost += costCols[initC]

    return cost
