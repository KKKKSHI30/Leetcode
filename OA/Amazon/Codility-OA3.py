def Solution(A):
    max_number = 0
    for i in A:
        if i >= 0 and i < 10:
            if i > max_number:
                max_number = i
    return max_number


Solution([-6, -91, 1011, -100, 84, -22, 0, 1, 473])


def Solution2(numbers):
    minimum = numbers[0]
    for i in numbers:
        if i < minimum:
            minimum = i
    print(minimum)


Solution2([-6, -91, 1011, -100, 84, -22, 0, 1, 473])

import itertools
def unique_permutations(elements):
    if len(elements) == 1:
        yield (elements[0],)
    else:
        unique_elements = set(elements)
        for first_element in unique_elements:
            remaining_elements = list(elements)
            remaining_elements.remove(first_element)
            for sub_permutation in unique_permutations(remaining_elements):
                yield (first_element,) + sub_permutation

def Solution3(A, B, C, D):
    valid = 0
    perm = unique_permutations([A,B,C,D])
    for i in perm:
        hour = i[0] * 10 + i[1]
        minute = i[2] * 10 + i[3]
        if hour < 24 and minute < 60:
            valid += 1
    return valid


Solution3(1, 8, 3, 2)
Solution3(2, 3, 3, 2)
Solution3(6, 2, 4, 7)




list(unique_permutations((1,1,2)))