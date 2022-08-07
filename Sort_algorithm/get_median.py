# Ke Shi on July 29th, 2022

import heapq
class min_heap:
    def __init__(self, val):
        self.val = val

    def __lt__(self, other,):
        return self.val < other.val

class max_heap:
  def __init__(self, val):
      self.val = val

  def __lt__(self, other):
      return self.val > other.val

def get_median():
    small_heap = []
    big_heap = []
    num = input("print a number in keyboard")
    while num:
        if num == "exit":
            break
        try:
            num = int(num)
        except:
            Exception("Cannot change to a number")

        if len(big_heap) == 0:
            heapq.heappush(big_heap, max_heap(num))
        else:
            top = heapq.heappop(big_heap).val
            if num <= top:
                heapq.heappush(big_heap, max_heap(top))
                heapq.heappush(big_heap, max_heap(num))
            else:
                heapq.heappush(small_heap, min_heap(num))
                heapq.heappush(big_heap, max_heap(top))

        if len(small_heap) - len(big_heap) == 2:
            heapq.heappush(big_heap, max_heap(heapq.heappop(small_heap).val))
        elif len(big_heap) - len(small_heap) == 2:
            heapq.heappush(small_heap, min_heap(heapq.heappop(big_heap).val))

        if (len(small_heap) + len(big_heap)) % 2 == 0:
            big = heapq.heappop(big_heap).val
            small = heapq.heappop(small_heap).val
            print(f"median is {(big + small) / 2}")
            heapq.heappush(big_heap, max_heap(big))
            heapq.heappush(small_heap, min_heap(small))
        elif len(small_heap) > len(big_heap):
            cur = heapq.heappop(small_heap).val
            print(f"median is {cur}")
            heapq.heappush(small_heap, min_heap(cur))
        else:
            cur = heapq.heappop(big_heap).val
            print(f"median is {cur}")
            heapq.heappush(big_heap, max_heap(cur))
        num = input("print a number in keyboard")

get_median()