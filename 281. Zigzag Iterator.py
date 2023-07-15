# Two-Pointers
# Time: next: O(k), hasNext: O(1)
# Space: next: O(k), hasNext: O(k)
# 2023.07.07: no
from collections import deque


class ZigzagIterator:
    def __init__(self, v1, v2):
        self.vectors = [v1, v2]
        self.p_elem = 0   # pointer to the index of element
        self.p_vec = 0    # pointer to the vector
        # variables for hasNext() function
        self.total_num = len(v1) + len(v2)
        self.output_count = 0

    def next(self):
        iter_num = 0
        ret = None

        # Iterate over the vectors
        while iter_num < len(self.vectors):
            curr_vec = self.vectors[self.p_vec]
            if self.p_elem < len(curr_vec):
                ret = curr_vec[self.p_elem]

            iter_num += 1
            self.p_vec = (self.p_vec + 1) % len(self.vectors)
            # increment the element pointer once iterating all vectors
            if self.p_vec == 0:
                self.p_elem += 1

            if ret is not None:
                self.output_count += 1
                return ret

        # no more element to output
        raise Exception


    def hasNext(self):
        return self.output_count < self.total_num
# Queue of Pointers
# Time: next: O(1), hasNext: O(1)
# Space: next: O(k), hasNext: O(k)
# 2023.07.07: no
class ZigzagIterator2:
    def __init__(self, v1, v2):
        self.vectors = [v1, v2]
        self.queue = deque()
        for index, vector in enumerate(self.vectors):
            # <index_of_vector, index_of_element_to_output>
            if len(vector) > 0:
                self.queue.append((index, 0))

    def next(self):

        if self.queue:
            vec_index, elem_index = self.queue.popleft()
            next_elem_index = elem_index + 1
            if next_elem_index < len(self.vectors[vec_index]):
                # append the pointer for the next round
                # if there are some elements left
                self.queue.append((vec_index, next_elem_index))

            return self.vectors[vec_index][elem_index]

        # no more element to output
        raise Exception

    def hasNext(self) -> bool:
        return len(self.queue) > 0


# Tests:
i, v = ZigzagIterator2(v1 = [1,2], v2 = [3,4,5,6]), []
while i.hasNext():
    v.append(i.next())