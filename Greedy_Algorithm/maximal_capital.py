# Ke Shi on Aug 2nd, 2022
import heapq

class node:
    def __init__(self, profit, cost):
        self.profit = profit
        self.cost = cost

    def __lt__(self, other,):
        return self.cost < other.cost

# method: get a new object and resign the __lt__
class MaxHeapObj(object):
  def __init__(self, profit, cost):
      self.profit = profit
      self.cost = cost

  def __lt__(self, other):
      return self.profit > other.profit

# 定义不清楚
def find_max_capital(k, wallet, profits, costs):
    mincost_lock = []
    maxprofit = []
    for i in range(len(profits)):
        heapq.heappush(mincost_lock, node(profits[i], costs[i]))
    for j in range(k):
        while len(mincost_lock) != 0:
            cur = heapq.heappop(mincost_lock)
            if cur.cost < wallet:
                heapq.heappush(maxprofit, MaxHeapObj(cur.profit, cur.cost))
            if len(maxprofit) == 0:
                return wallet
            wallet += heapq.heappop(maxprofit).profit
    return wallet

profits = [1,1,2,3,2,4]
costs = [1,4,3,2,7,10]
k = 5
wallet = 3
find_max_capital(k, wallet, profits, costs)
