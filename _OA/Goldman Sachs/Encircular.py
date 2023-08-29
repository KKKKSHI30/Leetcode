# 题目: https://www.1point3acres.com/bbs/thread-1010638-1-1.html
def doesCircleExists(comments):
    def bounded(instructions):
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        x = y = 0
        idx = 0
        for i in instructions:
            if i == "L":
                idx = (idx + 3) % 4
            elif i == "R":
                idx = (idx + 1) % 4
            else:
                x += directions[idx][0]
                y += directions[idx][1]
        return (x == 0 and y == 0) or idx != 0
    results = []
    for comment in comments:
        results.append(bounded(comment))
    return results
doesCircleExists(["G", "L", "RGRG"])


