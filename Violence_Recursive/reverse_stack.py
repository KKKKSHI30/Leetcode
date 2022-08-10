# Ke Shi on Aug 8th, 2022
from queue import LifoQueue
def reverse_stack(q):
    if q.empty():
        return
    i = first(q)
    reverse_stack(q)
    q.put(i)
    return q

def first(q):
    result = q.get()
    if q.empty():
        return result
    else:
        last = first(q)
        q.put(result)
    return last

test1 = LifoQueue()
test1.put(1)
test1.put(2)
test1.put(3)
result1 = reverse_stack(test1)