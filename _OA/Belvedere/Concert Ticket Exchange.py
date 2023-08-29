# 题目意思，记录orderID和artist，然后看要不要删掉这个orderID
import sys
import heapq
class AddOrder():
    def __init__(self, orderId, artist, price, quantity):
        self.orderId = int(orderId)
        self.artist = str(artist)
        self.price = float(price)
        self.quantity = float(quantity)
class ModifyOrder():
    def __init__(self, orderId, artist, price, quantity):
        self.orderId = int(orderId)
        self.artist = str(artist)
        self.price = float(price)
        self.quantity = float(quantity)
class DeleteOrder():
    def __init__(self, orderId, artist):
        self.orderId = int(orderId)
        self.artist = str(artist)
class DeletePriceLevel():
    def __init__(self, artist, price):
        self.artist = str(artist)
        self.price = int(price)

class PriceLadder():
    def __init__(self):
        self.artist_based = {}  # artist: orderID          主要目的是看artist有哪些order，最后可以提取出来排序
        self.price_based = {}   # price: artist, orderID   主要目的是拿到price，根据artist然后orderID从order里删掉数据
        self.order_based = {}   # order: artist, price, quantity  # 可以直接根据orderID删掉数据
    def AddOrder(self, order):
        if order.artist not in self.artist_based:
            self.artist_based[order.artist] = [order.orderId]
        else:
            self.artist_based[order.artist].append(order.orderId)
        if order.price not in self.price_based:
            self.price_based[int(order.price)] = [(order.artist, order.orderId)]
        else:
            self.price_based[int(order.price)].append((order.artist, order.orderId))
        self.order_based[order.orderId] = [order.artist, order.price, order.quantity]

    def DeleteOrder(self, delete):
        price = self.order_based[delete.orderId][1]
        self.order_based.pop(delete.orderId)
        self.artist_based[delete.artist].remove(delete.orderId)
        self.price_based[price].remove((delete.artist, delete.orderId))
        if not self.price_based[price]:
            del self.price_based[price]

    def DeletePriceLevel(self, deletePriceLevel):
        delStaff = self.price_based[deletePriceLevel.price]
        for del_artist, del_orderID in delStaff:
            if del_artist == deletePriceLevel.artist:
                self.DeleteOrder(DeleteOrder(del_orderID, del_artist))

    def GetPriceLevels(self, artist, numberOfPriceLevels):
        print(artist)
        orders = self.artist_based[artist]
        all_values = {}
        index = -1
        for i in orders:
            index += 1
            order = self.order_based[i]
            if (order[0], order[1]) in all_values:
                self.order_based[all_values[(order[0], order[1])]][2] += order[2]
                self.order_based.pop(i)
                orders.pop(index)
            else:
                all_values[(order[0], order[1])] = i
        h = []
        h2 = []
        temp = []
        for i in orders:
            heapq.heappush(h, [self.order_based[i][1], self.order_based[i][2]])
            heapq.heappush(h2, [-self.order_based[i][1], self.order_based[i][2]])
        time = 0
        while time < numberOfPriceLevels:
            temp_price, temp_quantity = heapq.heappop(h)
            if temp_quantity < 0:
                temp.append(f"0 {int(temp_price)} {-int(temp_quantity)}")
                time += 1
            else:
                heapq.heappush(h2, [temp_price, temp_quantity])
        temp.reverse()
        for i in temp:
            print(i)
        time = 0
        while time < numberOfPriceLevels:
            temp_price, temp_quantity = heapq.heappop(h2)
            if temp_quantity > 0:
                print(f"{int(temp_quantity)} {-int(temp_price)} 0")
                time += 1

priceLadder = PriceLadder()
for line in sys.stdin:
    tokens = line.split()
    if tokens[0] == "ADD":
        priceLadder.AddOrder(AddOrder(*tokens[1:]))
    elif tokens[0] == "DEL":
        priceLadder.DeleteOrder(DeleteOrder(*tokens[1:]))
    elif tokens[0] == "DEL_PRICE":
        priceLadder.DeletePriceLevel(DeletePriceLevel(*tokens[1:]))
    else:
        artist = tokens[0]
        numberOfPriceLevels = int(tokens[1])
        priceLadder.GetPriceLevels(artist, numberOfPriceLevels)

"""
ADD 1 TaylorSwift 100  10
ADD 2 TaylorSwift 101 -10
ADD 3 TaylorSwift 99   5
ADD 4 TaylorSwift 102 -5
ADD 5 TaylorSwift 100  2
DEL 1 TaylorSwift
TaylorSwift 2

buy price sell
     101  10
5    99
     102   5
2   100

      102   5
      101   10
2     100
5     99



ADD 1 TaylorSwift 100  10
ADD 2 TaylorSwift 101 -10
ADD 3 TaylorSwift 99   5
ADD 4 TaylorSwift 102 -5
ADD 5 TaylorSwift 98 2
ADD 6 TaylorSwift 99   5
DEL_PRICE TaylorSwift 100
TaylorSwift 1

# 卖的价格需要最低
buy price sell
0  101   10
10 99    0

"""
















