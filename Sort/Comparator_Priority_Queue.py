# Ke Shi on Feb 20th, 2022
from queue import PriorityQueue

class CustomPriorityQueue(PriorityQueue):
    def _put(self, item):
        return super()._put((self._get_priority(item), item))

    def _get(self):
        return super()._get()[1]


    def _get_priority(self, item):
        return item[1]

q = CustomPriorityQueue(100)
q.put((2, 3, 5))
q.put((2, 5, 5))
q.put((2, 1, 5))
q.put((2, 2, 5))
q.get()