# BFS
# Time: O(n^2*a^n+D)
# Space: O(a^n+D)
# 2023.08.04: yes
# notes: continue, 不是return
from collections import deque
class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        q = deque()
        q.append("0000")
        visited = set()
        step = -1
        while q:
            step += 1
            size = len(q)
            for j in range(size):
                cur = q.popleft()
                if cur in visited:
                    continue
                else:
                    visited.add(cur)
                if cur == target:
                    return step
                if cur in deadends:
                    continue
                for i in range(4):
                    if cur[i] == '9':
                        q.append(cur[:i] + "0" + cur[i + 1:])
                        q.append(cur[:i] + str(int(cur[i])-1) + cur[i + 1:])
                    elif cur[i] == '0':
                        q.append(cur[:i] + str(int(cur[i])+1) + cur[i + 1:])
                        q.append(cur[:i] + '9' + cur[i + 1:])
                    else:
                        q.append(cur[:i] + str(int(cur[i])+1) + cur[i+1:])
                        q.append(cur[:i] + str(int(cur[i])-1) + cur[i + 1:])
        return -1

# BFS double end
# Time: O(n^2*a^n+D)
# Space: O(a^n+D)
# 2023.08.04: no
# notes: 这道题可以双向BFS，可以加快速度
class Solution2(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        deadends = set(deadends)
        visited = set('0000')
        step = 0
        q1 = set()
        q2 = set()
        q1.add('0000')
        q2.add(target)
        while len(q1) != 0 and len(q2) != 0:
            temp = set()
            # put all q1's neighbour into temp
            for i in q1:
                if i in deadends:
                    continue
                if i in q2:
                    return step
                visited.add(i)
                for j in range(4):
                    up = self.plusone(i, j)
                    if up not in visited:
                        temp.add(up)
                    down = self.minusone(i, j)
                    if down not in visited:
                        temp.add(down)
            step+=1
            # change q1, q2
            q1 = q2
            q2 = temp
        return -1

    def plusone(self, s, j):
        s = list(s)
        if s[j] == '9':
            s[j] = '0'
        else:
            s[j] = int(s[j])+1
        s = [str(i) for i in s]
        return "".join(s)

    def minusone(self, s, j):
        s = list(s)
        if s[j] == '0':
            s[j] = '9'
        else:
            s[j] = int(s[j])-1
        s = [str(i) for i in s]
        return "".join(s)



# A* Search
# Time: O(8^d)
# Space: O(n)
# 2023.08.04: no
from queue import PriorityQueue

class Solution3:
    def openLock(self, deadends, target):
        def h(node):
            dist = 0
            for i in range(4):
                dist += min((int(node[i]) - int(target[i])) % 10, (int(target[i]) - int(node[i])) % 10)
            return dist

        start = "0000"
        if start == target:
            return 0

        deadends = set(deadends)
        if start in deadends:
            return -1

        visited = set(start)

        queue = PriorityQueue()
        queue.put((h(start), start))

        while not queue.empty():
            f, node = queue.get()

            for i in range(4):
                for move in [-1, 1]:
                    new_digit = (int(node[i]) + move) % 10
                    neighbor = node[:i] + str(new_digit) + node[i+1:]

                    if neighbor in deadends or neighbor in visited:
                        continue

                    if neighbor == target:
                        return f

                    visited.add(neighbor)
                    queue.put((f - h(node) + 1 + h(neighbor), neighbor))

        return -1

test = Solution()
test.openLock(['8888'], '1000')
test.openLock(["0201","0101","0102","1212","2002"], "0202")
test.openLock(["8887","8889","8878","8898","8788","8988","7888","9888"], '8888')
