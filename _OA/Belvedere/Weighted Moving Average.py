def WMA(trades):
    results = {}
    largest_sequence = float('-inf')
    trades = trades.split(';')
    for trade in trades:
        key, value, quantity, sequence_number = trade.split(",")
        key, value, quantity, sequence_number = int(key), int(value), int(quantity), int(sequence_number)
        if sequence_number >= largest_sequence:
            if key not in results:
                Mx, Qx = 0, 0
            else:
                Mx, Qx = results[key]
            Mx = ((Mx*Qx)+(value*quantity))/(Qx+quantity)
            Qx = Qx + quantity
            results[key] = (Mx, Qx)
            largest_sequence = sequence_number
            print(f"{key}:{'{:.2f}'.format(Mx)}")



WMA("1,2000,5,1;1,2050,5,2;2,3000,10,3")
WMA("1,2000,5,1;1,2030,15,2;1,2000,10,1;2,2050,15,5;1,2067,8,6;2,2050,5,7")
WMA("1,2000,5,1;2,2050,15,2")
WMA("1,2000,5,2;1,2050,5,4")
WMA("1,2000,5,3;2,2040,5,2")