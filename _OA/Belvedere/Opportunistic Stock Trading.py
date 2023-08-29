import sys

class Bundle:
    def __init__(self, name, price, components):
        self.name = name
        self.price = price
        self.components = components

class Stock:
    def __init__(self, name, price):
        self.name = name
        self.price = price

def PrintTrade(name, bundleOrStock, price):
    p = "{:.2f}".format(price)
    print("{} E {} {}".format(name, bundleOrStock, p))

def PrintNoTrade(name):
    print("{} P".format(name))

class MarketWatchPortfolio:
    def __init__(self, bundles, stocks):
        self.bundles = bundles
        self.stocks = stocks

    def ExecuteTrades(self):
        for bundle in self.bundles:
            current_values = 0
            not_in_stock = False
            for component in bundle.components:
                if component[1] not in self.stocks:
                    PrintNoTrade(bundle.name)
                    not_in_stock = True
                else:
                    current_values += int(component[0])*self.stocks[component[1]].price
            if not_in_stock:
                continue
            if current_values >= bundle.price:
                PrintTrade(bundle.name,"B",bundle.price)
            else:
                PrintTrade(bundle.name,"I",current_values)
            self.stocks[bundle.name] = min(current_values, bundle.price)


# commend + D
def ParseInputs():
    bundles = list()
    stocks = dict()
    num_stocks = -1
    num_bundles = -1
    for line in sys.stdin:
        parsed = line.strip().split(' ')
        if num_bundles == -1 and num_stocks == -1:
            num_bundles = int(parsed[0])
            num_stocks = int(parsed[1])
            continue
        if num_bundles > 0:
            components = list()
            for i in range(3, len(parsed) - 1, 2):
                components.append((int(parsed[i + 1]), parsed[i]))
            bundles.append(Bundle(parsed[0], float(parsed[1]), components))
            num_bundles -= 1
            continue
        try:
            s = Stock(parsed[0], float(parsed[1]))
        except:
            break
        stocks[parsed[0]] = s
    return MarketWatchPortfolio(bundles, stocks)

def main():
    portfolio = ParseInputs()
    portfolio.ExecuteTrades()

if __name__ == '__main__':
    main()


"""
Test1
3 5
apx 99.5 3 aapl 4 amzn 3 aarp 4
spj 200.0 2 spy 3 swg 2
sspx 65 2 spy 1 aapl 1
aapl 10.5
amzn 12.0
aarp 5.0
spy 45.0
swg 33.5

output
apx E I 98.00
spj E B 200.00
sspx E I 55.50

Test2:
2 4
adgb 5404.0 3 tadb 2 goog 2 meta 1
tadb 2520.0 2 bbby 5 hmny 4
goog 125.0
meta 114.0
bbby 225.0
hmny 350.75

output:
adgb P
tadb E B 2520.00

Test3:
2 4
adgb 5402.0 3 tadb 2 goog 2 meta 1
tadb 2530.0 2 bbby 5 hmny 4
goog 125.0
meta 114.0
bbby 225.0

output:
adgb P
tadb P

"""