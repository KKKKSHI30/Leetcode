# Ke Shi on Aug 8th, 2022

# 第一个超重时返回0，已经加上了超重之后的值，因为递归返回值是累加的；第二种方法超重返回0是直接吧总值设为0，所以不会出现比不超重情况的总值大的情况
def most_value(weights, values, limit_weight):
    return process(weights, values,0, 0, limit_weight)

def process(weights, values, i, already_weight, limit_weight):
    if already_weight > limit_weight:
        return 0
    if i == len(weights):
        return 0
    return max(process(weights, values, i+1, already_weight, limit_weight),
               values[i] + process(weights, values, i+1, already_weight + weights[i], limit_weight)
               )

def most_value2(weight, values, limit_weight):
    return process2(weight, values, 0, 0, 0, limit_weight)

def process2(weights, values, i, already_weight, already_value, limit_weight):
    if already_weight > limit_weight:
        return 0
    if i == len(values):
        return already_value
    return max(process2(weights, values, i+1, already_weight, already_value, limit_weight),
               process2(weights, values, i+1, already_weight+weights[i], already_value+values[i], limit_weight)
               )


limit_weight = 15
weight = [1,2,3,4,5,1]
values = [6,2,3,7,2,3]
result = most_value(weight, values, limit_weight)
result2 = most_value2(weight, values, limit_weight)
