from collections import deque
def max_window(lstOfNum, w):
    window = deque()
    if lstOfNum == None or w < 1 or w > len(lstOfNum):
        return None
    index = 0
    res = []
    window.append(0)
    for i in range(1,len(lstOfNum)):
        while len(window) != 0 and lstOfNum[window[0]] <= lstOfNum[i]:
            window.pop()
        window.append(i)
        if window[0] == i - w: # 标过期了
            window.popleft()
        if (i >= w-1):  # 窗口形成
            res.append(lstOfNum[window[0]])
            index+= 1
    return res

max_window([4,3,5,4,3,3,6,7], 3)

def max_window2(lstOfNum, directions):
    window = deque()
    if lstOfNum == None or len(directions) < 1:
        return None
    left = 0
    right = 0
    res = []
    for i in range(len(lstOfNum)):
        if directions[i] == "R":
            right += 1
            while len(window) != 0 and lstOfNum[window[0]] <= lstOfNum[i]:
                window.pop()
            window.append(i)
        else:
            left += 1
            if window[0] == left:
                window.popleft()
        res.append(lstOfNum[window[0]])
    return res

max_window2([4,3,5,4,3,3,6,7], ["R", "R", "R", "R", "L", "L", "R", "R", "R", "L", "R", "L", "L"])






