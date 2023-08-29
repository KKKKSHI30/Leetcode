# buy = TheoreticalValue−TradePrice
# sell = TradePrice−TheoreticalValue
# Traders typically want to execute trades that have positive edge, that is buying an asset for lower than the theoretical value, or selling an asset for higher than the theoretical value.
# For example: TradePrice = 95, TheoreticalValue = 100, Edge = 100-95 = 5
# As a Firm, we want to track which traders are making the best decisions, so we calculate a score for each trade.
# Score=SignOfEdge(Edge^2*∣Quantity∣)
import sys
class Trade():
    def __init__(self, trader, asset, quantity, price):
        self.Trader = trader
        self.Asset = asset
        self.Quantity = quantity
        self.Price = price
class TheoUpdate():
    def __init__(self, asset, value):
        self.Asset = asset
        self.Value = value
def ParseTrade(line):
    args = line.split(" ")
    # args[0] is "Trade"
    return Trade(str(args[1]), int(args[2]), int(args[3]), float(args[4]))
def ParseTheoUpdate(line):
    args = line.split(" ")
    # args[0] is "TheoUpdate"
    return TheoUpdate(int(args[1]), float(args[2]))
def PrintTraderScore(traderName, score):
    print(traderName, "{:.2f}".format(score))

class TradeAggregator():
    def __init__(self):
        self.theo = {}
        self.person_score = {}
    def HandleTrade(self, trade):
        if trade.Asset not in self.theo:
            self.theo[trade.Asset] = trade.Price
            self.person_score[trade.Trader] = 0
        else:
            if trade.Trader not in self.person_score:
                if trade.Quantity > 0:
                    self.person_score[trade.Trader] = (self.theo[trade.Asset] - trade.Price) ** 2 * trade.Quantity
                else:
                    self.person_score[trade.Trader] = (trade.Price - self.theo[trade.Asset]) ** 2 * (-trade.Quantity)
            else:
                if trade.Quantity > 0:
                    self.person_score[trade.Trader] += (self.theo[trade.Asset] - trade.Price) ** 2 * trade.Quantity
                else:
                    self.person_score[trade.Trader] += (trade.Price - self.theo[trade.Asset]) ** 2 * (-trade.Quantity)

    def HandleTheoUpdate(self, theoUpdate):
        self.theo[theoUpdate.Asset] = theoUpdate.Value

    def PrintBestScore(self):
        max_key = None
        max_value = float('-inf')

        for key, value in self.person_score.items():
            if value > max_value:
                max_key = key
                max_value = value
        PrintTraderScore(max_key, max_value)

tradeAgg = TradeAggregator()
for line in sys.stdin:
    if line.find("Trade") != -1:
        trade = ParseTrade(line)
        tradeAgg.HandleTrade(trade)
        tradeAgg.PrintBestScore()
    else:
        theoUpdate = ParseTheoUpdate(line)
        tradeAgg.HandleTheoUpdate(theoUpdate)


"""
# 如果theo没有的话，第一个遇到的就是theo
# 第一个1是theo, 第二个1是正，所以是100 - 95
# 第二个-1， 所以是107-100 
Test1:
TheoUpdate 1 100
Trade Alice 1 1 95   
Trade Bob 1 1 94
Trade Alice 1 -1 107 

Alice 25.00
Bob 36.00
Alice 74.00

Test2:
TheoUpdate 1 100
Trade Alice 1 -2 101
Trade Bob 1 -2 99

Alice 2.00
Alice 2.00

Test3:
TheoUpdate 1 100
Trade Alice 1 400 99
Trade Bob 1 5 90

Alice 400.00
Bob 500.00

Test4:
TheoUpdate 1 100
TheoUpdate 2 200
Trade Alice 1 1 98
Trade Bob 2 1 199

Alice 4.00
Alice 4.00

"""
