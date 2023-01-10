# Ke Shi on July 31th, 2022
import heapq
# testing heapq using
a = []
heapq.heappush(a, 2)
heapq.heappush(a, 2)
heapq.heappush(a, 3)
heapq.heappush(a, 4)
heapq.heappop(a)


def less_money(lst_of_cuts):
    money_heap = []
    for i in lst_of_cuts:
        heapq.heappush(money_heap, i)
    total = 0
    while (len(money_heap) > 2):
        cur_total = heapq.heappop(money_heap) + heapq.heappop(money_heap)
        total += cur_total
        heapq.heappush(money_heap, cur_total)
    return total


cuts = [2,2,3,4,7,9]

less_money(cuts)

