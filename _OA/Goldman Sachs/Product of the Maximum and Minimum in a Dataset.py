def minMax(operations):
    result = []
    cur_value = 1
    cur_pop_value = 1
    cur_result = 1
    for operation in operations:
        if operation == "push":
            cur_result *= cur_value
            cur_value += 1
            result.append(cur_result)
        else:
            cur_result /= cur_pop_value
            cur_result = int(cur_result)
            cur_pop_value += 1
            result.append(cur_result)
    return result

minMax(["push", "push", "push", "pop"])