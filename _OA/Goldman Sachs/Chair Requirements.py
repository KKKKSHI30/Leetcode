# 题目: https://www.1point3acres.com/bbs/thread-1009988-1-1.html
def min_chairs(simulations):
    min_chairs = []

    for simulation in simulations:
        occupied_chairs = 0
        total_chairs = 0

        for action in simulation:
            if action == 'C' or action == 'U':
                if total_chairs == occupied_chairs:
                    total_chairs += 1
                occupied_chairs += 1
            elif action == 'R' or action == 'L':
                occupied_chairs -= 1
        min_chairs.append(total_chairs)

    return min_chairs

min_chairs(["CCRUCL", "CRUC", "CCC"])
min_chairs(["CCCRRR", "CC", "CCRURC"])
