# 题目: https://www.1point3acres.com/bbs/thread-1010658-1-1.html
def maxProfit(costPerCut, salePrice, lengths):
    max_profit = 0
    for sale_length in range(1, max(lengths) + 1):
        sale_price_per_rod = salePrice * sale_length
        profit = 0
        for rod_length in lengths:
            uniform_rods = rod_length // sale_length
            if uniform_rods > 0:
                extra_cut = 1 if rod_length % sale_length > 0 else 0
                total_cuts = uniform_rods - 1 + extra_cut
                costs = total_cuts * costPerCut
                revenues = uniform_rods * sale_price_per_rod
                if revenues > costs:
                    profit += revenues - costs
        max_profit = max(profit, max_profit)
    return max_profit

maxProfit(1, 10, [30, 59, 110])
maxProfit(1,10, [26, 103, 59])