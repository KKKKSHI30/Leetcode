def grid_shot(grid, shots):
    ship_length = {}
    visited = []
    result = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] not in ship_length:
                ship_length[grid[i][j]] = 1
            else:
                ship_length[grid[i][j]] += 1
    for shot in shots:
        x, y = shot[0], shot[1]
        if shot in visited and grid[x][y] != '.':
            result.append('Already attacked')
        elif grid[x][y] == '.':
            result.append('Missed')
        else:
            visited.append(shot)
            ship_length[grid[x][y]] -= 1
            if ship_length[grid[x][y]] == 0:
                result.append(f"Ship {grid[x][y]} sunk")
            else:
                result.append(f"Attacked ship {grid[x][y]}")
    return result


grid = [['.', 'A', 'B', 'B', 'B'],
        ['.', 'A', '.', '.', 'C'],
        ['.', '.', '.', '.', '.'],
        ['D', 'D', '.', '.', '.'],
        ['.', 'E', 'E', 'E', 'E']]
shots = [[0,0],[0,1],[0,2],[1,1],[0,1],[1,4],[2,2],[2,4],[0,3],[0,0],[0,4]]
grid_shot(grid, shots)
# [Missed, Attacked Ship A, Attacked Ship B, Ship A sunk, Already attacked,
# Ship C sunk, Missed, Missed, Attacked Ship B, Missed, Ship B sunk]