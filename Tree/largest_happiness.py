class Employee(object):
    def __init__(self, happiness, subordinates = []):
        self.happiness = happiness
        self.subordinates = subordinates

def max_happiness(head):
    come, not_come = process(head)
    return max(come, not_come)

def process(head):
    if len(head.subordinates) == 0:
        return head.happiness, 0
    come = head.happiness
    not_come = 0
    for i in head.subordinates:
        come_sub, not_come_sub = process(i)
        come += not_come_sub
        not_come += max(come_sub, not_come_sub)
    return come, not_come

test = Employee(100, [Employee(10, [Employee(5), Employee(200)]), Employee(20, [Employee(50), Employee(5)]), Employee(30)])
max_happiness(test)

