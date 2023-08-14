def manufacture():
    target = input()  # Read the target item
    saving = {}
    prices = {}
    while True:
        line = input()
        if not line:  # Stop if the line is empty
            break
        name, price, size, input_products = line.split(",")
        if price == None or price == "None":
            saving[name] = ([None, int(size), input_products])
        else:
            saving[name] = ([float(price), int(size), input_products])
    def recursion(item):
        if item in prices:
            return prices[item]
        if saving[item][2] == "":
            prices[item] = saving[item][0]
            return saving[item][0]
        items = saving[item][2].split(";")
        total = 0
        for i in items:
            total += recursion(i)
        if saving[item][0] == None:
            return total
        min_total =  min(total, saving[item][0])
        prices[item] = min_total
        return min_total
    return print(recursion(target))
manufacture()

"""
Test1:
teddy bear
painted glass eyeball,10.5,2,glass;paint
glass,5,0,
paint,4,0,
teddy bear,null,4,painted glass eyeball;tiny shirt;faux bear fur fabric;sewing thread
faux bear fur fabric,15,2,bear;yarn
bear,100,0,
yarn,2,0,
sewing thread,13,0,
tiny shirt,24,0,

Test2:
car
car,30000,5,seat;steering wheel;carpet;windshield;radio
radio,200,0,
steering wheel,None,3,leather;plastic;foam
seat,None,3,leather;foam;plastic
plastic,1300,0,
foam,7000,0,
leather,4000,0,
carpet,1000,1,plastic
windshield,5000,1,glass
glass,2000,1,sand
sand,0,0,

Test3:
office chair
wheels,3.5,2,plastic;metal
cushioned seat,7.5,3,screws;padding;leather
screws,1.5,1,metal
arm rests,5,3,padding;plastic;leather
lumbar support,15,4,plastic;padding;leather;screws
plastic,2,0,
padding,3,0,
leather,4,0,
metal,1,0,
office chair, 26.25,5,wheels;cushioned seat;screws;arm rests;lumbar support
"""

