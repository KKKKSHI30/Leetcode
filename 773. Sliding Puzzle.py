# Breadth First Search
# Time: O(mn)
# Space: O(1)
# 2023.07.31: no
# notes: 这道题很难想到的点是怎么去确定这个2*3的matrix永远不可能成为"123450"，方法是用BFS，记录所有有可能的状态
# 如果所有的状态都走完了，那么当前2*3是不可能有解的，否则只要返回步数即可，其中的第一个技巧是2*3的数组，我们用1*6的string
# 来标答，方便map，因为对于任何0的位置都只有4中可能，上下左右，左右就是+1，-1，上下就是+col, -col，只要保证变化后的
# 数字在这个string中即为有效，第二点是因为我们要求步数，所以一次把能Push的点都push完，全部即为一步，再把由这些点
# 可能的所有变化push，即为第二步，所以第一个for loop表示当前dq中的所有当前步数的节点，把当前dq检查一遍后，step才会+1
import collections
import heapq


class Solution(object):
    def slidingPuzzle(self, board):
        s = "".join(str(d) for row in board for d in row)
        dq, seen = collections.deque(), {s}
        dq.append((s, s.index("0")))
        steps, height, width = 0, len(board), len(board[0])
        while dq:
            for _ in range(len(dq)):
                t, i = dq.popleft()
                if t == "123450":
                    return steps
                x, y = i // width, i % width
                for r, c in (x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y):
                    if height > r >= 0 <= c < width:
                        ch = [d for d in t]
                        ch[i], ch[r * width + c] = ch[r * width + c], "0"
                        s = "".join(ch)
                        if s not in seen:
                            seen.add(s)
                            dq.append((s, r * width + c))
            steps += 1
        return -1


# A* Search
# Time: O(mn)
# Space: O(1)
# 2023.07.31: no
# notes: Dijkstra的进化版本，分为两个部分，当前状态（走了几步），到达重点的距离，这里用manhatten distance
# 对应的是heuristic，计算的是每个点距离正确的点的距离，全部加起来就是count，和dijkstra一样，把比当前小的状态
# 压进去，保证只会更小，不会更大，同时也要设置一个end状态，碰到那个状态，证明这道题无解，或者q空了也无解
class Solution2(object):
    def slidingPuzzle(self, board):
        goal = [[1, 2, 3], [4, 5, 0]]
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        def heuristic(board):
            count = 0
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] != 0:
                        x, y = int((board[i][j] - 0.1) / 3), (board[i][j] - 1) % 3
                        count += abs(x - i) + abs(y - j)
            return count

        def a_star(start):
            q = []
            heapq.heappush(q, (0, start))
            cost = {}
            cost[str(start)] = 0

            while q:
                board_now = heapq.heappop(q)[1]
                if heuristic(board_now) == 0:
                    break
                i, j = 0, 0
                for i in range(len(board_now)):
                    for j in range(len(board_now[i])):
                        if board_now[i][j] == 0:
                            break
                    if board_now[i][j] == 0:
                        break

                for directions in range(4):
                    nx = i + dx[directions]
                    ny = j + dy[directions]
                    if (
                        nx < len(board_now)
                        and nx >= 0
                        and ny >= 0
                        and ny < len(board_now[0])
                    ):
                        board_next = [[0] * 3, [0] * 3]
                        board_next[0][:] = board_now[0]
                        board_next[1][:] = board_now[1]
                        board_next[i][j] = board_next[nx][ny]
                        board_next[nx][ny] = 0
                        if (
                            str(board_next) not in cost
                            or cost[str(board_now)] + 1 < cost[str(board_next)]
                        ):
                            cost[str(board_next)] = cost[str(board_now)] + 1
                            priority = cost[str(board_now)] + 1 + heuristic(board_next)
                            heapq.heappush(q, (priority, board_next))
            if str(goal) in cost:
                return cost[str(goal)]
            return -1

        return a_star(board)


# Tests:
test = Solution2()
test.slidingPuzzle(board=[[1, 2, 3], [4, 0, 5]])
