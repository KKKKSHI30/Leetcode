import queue
class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        deadends = set(deadends)
        visited = set('0000')
        step = 0
        q = queue.Queue()
        q.put('0000')
        while not q.empty():
            sz = q.qsize()
            for i in range(sz):
                cur = q.get()
                if cur in deadends:
                    continue
                if cur == target:
                    return step
                for j in range(4):
                    up = self.plusone(cur, j)
                    if up not in visited:
                        visited.add(up)
                        q.put(up)
                    down = self.minusone(cur, j)
                    if down not in visited:
                        visited.add(down)
                        q.put(down)
            step+=1
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


test = Solution()
test.openLock(["0201","0101","0102","1212","2002"], "0202")
test.openLock(['8888'], '0009')
test.openLock(["8887","8889","8878","8898","8788","8988","7888","9888"], '8888')

import queue
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
            q1= q2
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

test = Solution2()
test.openLock(["0201","0101","0102","1212","2002"], "0202")
test.openLock(['8888'], '0009')
test.openLock(["8887","8889","8878","8898","8788","8988","7888","9888"], '8888')
