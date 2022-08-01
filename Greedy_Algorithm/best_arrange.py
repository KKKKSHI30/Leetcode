# Ke Shi on July 29th, 2022

class program:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        return self.end < other.end

    def __gt__(self, other):
        return self.end > other.end

def best_arrange(meeting, timepoint):
    meeting_sorted = sorted(meeting, key=lambda program: program.end)
    result = 0
    for i in range(len(meeting_sorted)):
        if timepoint <= meeting_sorted[i].start:
            result += 1
            timepoint = meeting_sorted[i].end
    return result



a = program(6,7)
b = program(6,8)
c = program(7,9)
d = program(7,10)
e = program(8,11)
f = program(8,9)
g = program(9,10)
h = program(10,12)
meeting = [a, b, c, d, e, f, g, h]
meeting_sorted = sorted(meeting, key = lambda program:program.end)
result = best_arrange(meeting, 6)

