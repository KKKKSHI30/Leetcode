# risk = quantity*riskunit
# avgfillprice = sum(quantity*price_i)/ sum(quantity)

def naiveHedging():
    buy = input()
    sell = input()
    buy_quantity1, buy_price1, buy_quantity2, buy_price2, buy_quantity3, buy_price3 = buy.split(" ")
    buy_quantity1, buy_price1, buy_quantity2, buy_price2, buy_quantity3, buy_price3 = int(buy_quantity1), float(buy_price1), \
                                                                                      int(buy_quantity2), float(buy_price2), \
                                                                                      int(buy_quantity3), float(buy_price3)
    sell_quantity1, sell_price1, sell_quantity2, sell_price2, sell_quantity3, sell_price3 = sell.split(" ")
    sell_quantity1, sell_price1, sell_quantity2, sell_price2, sell_quantity3, sell_price3 = int(sell_quantity1), float(sell_price1), \
                                                                                            int(sell_quantity2), float(sell_price2), \
                                                                                            int(sell_quantity3), float(sell_price3)
    risk = 0
    while True:
        line = input()
        if not line:  # Stop if the line is empty
            break
        signed_quantity, risk_per_unit = line.split(" ")
        signed_quantity, risk_per_unit = int(signed_quantity), float(risk_per_unit)
        risk += signed_quantity*risk_per_unit
        risk_output, total_quantity = int(risk), -int(risk)
        risk -= risk_output
        total_fill_price = 0
        if risk_output <= 0:
            if buy_quantity1 != 0:
                if total_quantity <= buy_quantity1:
                    buy_quantity1 -= total_quantity
                    total_fill_price = total_quantity * buy_price1
                    print(f"{-risk_output} {'{:.2f}'.format(total_fill_price/total_quantity)}")
                    continue
                else:
                    total_quantity -= buy_quantity1
                    total_fill_price += buy_quantity1*buy_price1
                    buy_quantity1 = 0
            if buy_quantity2 != 0:
                if total_quantity <= buy_quantity2:
                    buy_quantity2 -= total_quantity
                    total_fill_price += total_quantity * buy_price2
                    print(f"{-risk_output} {'{:.2f}'.format(total_fill_price / total_quantity)}")
                    continue
                else:
                    total_quantity -= buy_quantity2
                    total_fill_price += buy_quantity2*buy_price2
                    buy_quantity2 = 0
            if buy_quantity3 != 0:
                buy_quantity3 -= total_quantity
                total_fill_price += total_quantity * buy_price3
                print(f"{-risk_output} {'{:.2f}'.format(total_fill_price / total_quantity)}")
        else:
            if sell_quantity1 != 0:
                if total_quantity <= sell_quantity1:
                    sell_quantity1 -= total_quantity
                    total_fill_price = total_quantity * sell_price1
                    print(f"{-risk_output} {'{:.2f}'.format(total_fill_price/total_quantity)}")
                    continue
                else:
                    total_quantity -= sell_quantity1
                    total_fill_price += sell_quantity1*sell_price1
                    sell_quantity1 = 0
            if sell_quantity2 != 0:
                if total_quantity <= sell_quantity2:
                    sell_quantity2 -= total_quantity
                    total_fill_price += total_quantity * sell_price2
                    print(f"{-risk_output} {'{:.2f}'.format(total_fill_price / total_quantity)}")
                    continue
                else:
                    total_quantity -= sell_quantity2
                    total_fill_price += sell_quantity2*sell_price2
                    sell_quantity2 = 0
            if sell_quantity3 != 0:
                sell_quantity3 -= total_quantity
                total_fill_price += total_quantity * sell_price3
                print(f"{-risk_output} {'{:.2f}'.format(total_fill_price / total_quantity)}")

naiveHedging()
"""
Test1: 
100 1850.00 200 1850.25 300 1850.50
100 1849.75 200 1849.50 300 1849.25
+10 0.20
+15 -0.20
-40 0.50
"""

