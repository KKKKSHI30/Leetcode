from collections import deque
def max_product_sublist(lstOfNum):
    # can use stack, deque can peak
    s = deque()
    max_value = 0
    if lstOfNum == None:
        return
    for i in range(len(lstOfNum)):
        while len(s) != 0:
            if lstOfNum[i] < lstOfNum[s[-1]]:
                temp = lstOfNum[s.pop()]
                if len(s) == 0:
                    max_value = max(max_value, sum(lstOfNum[0:i]) * lstOfNum[temp])
                    print(f"{temp}'s doesn't have left smaller and right smaller is {lstOfNum[i]}")
                    break
                max_value = max(max_value, sum(lstOfNum[s[-1]:i]) * lstOfNum[temp])
                print(f"{temp}'s left smaller is {lstOfNum[s[-1]]} and right smaller is {lstOfNum[i]}")
            else:
                break
        s.append(i)
    while len(s) > 1:
        max_value = max(max_value, sum(lstOfNum[s[-1]:]) * lstOfNum[s[-1]])
        print(f"{lstOfNum[s.pop()]}'s left smaller is {lstOfNum[s[-1]]} and doesn't have right smaller")
    max_value = max(max_value, sum(lstOfNum) * lstOfNum[s[-1]])
    print(f"{lstOfNum[s.pop()]} doesn't have a left smaller nor right smaller")
    return max_value

max_product_sublist([5,4,3,6,1,2,0,7])