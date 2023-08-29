from collections import deque

def minKnightMoves(n, startRow, startCol, endRow, endCol):
    offsets = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
    visited = set()
    queue = deque([(startRow, startCol)])
    steps = 0
    while queue:
        curr_level_cnt = len(queue)
        for i in range(curr_level_cnt):
            curr_x, curr_y = queue.popleft()
            if (curr_x, curr_y) == (endRow, endCol):
                return steps
            for offset_x, offset_y in offsets:
                next_x, next_y = curr_x + offset_x, curr_y + offset_y
                if next_x < 0 or next_x >= n or next_y < 0 or next_y >= n:
                    continue
                if (next_x, next_y) not in visited:
                    visited.add((next_x, next_y))
                    queue.append((next_x, next_y))
        steps += 1

# Example usage:
min_moves = minKnightMoves(9, 4, 4, 4, 8)
min_moves2 = minKnightMoves(9, 0, 0, 5, 5)
min_moves3 = minKnightMoves(9, 4, 4, 8, 8)

