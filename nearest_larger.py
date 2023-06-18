from collections import deque
def nearest_larger(lstOfNum):
    # can use stack, deque can peak
    s = deque()
    if lstOfNum == None:
        return
    for i in range(len(lstOfNum)):
        while len(s) != 0:
            if lstOfNum[i] > lstOfNum[s[-1]]:
                temp = lstOfNum[s.pop()]
                if len(s) == 0:
                    print(f"{temp}'s doesn't have left larger and right larger is {lstOfNum[i]}")
                    break
                print(f"{temp}'s left larger is {lstOfNum[s[-1]]} and right larger is {lstOfNum[i]}")
            else:
                break
        s.append(i)
    while len(s) > 1:
        print(f"{lstOfNum[s.pop()]}'s left larger is {lstOfNum[s[-1]]} and doesn't have right larger")
    print(f"{lstOfNum[s.pop()]} doesn't have a left larger nor right larger")

nearest_larger([5,4,3,6,1,2,0,7])