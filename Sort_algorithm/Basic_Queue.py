from queue import Queue  # 先进先出队列
from queue import PriorityQueue  # 优先级队列
import time

# 队列：先进先出
q = Queue()  # 创建一个空队列，队列大小没有指定
# 判断队列是是否为空
# 当一个队列为空的时候如果再用get取则会堵塞，所以取队列的时候一般是用到
# get_nowait()方法，这种方法在向一个空队列取值的时候会抛一个Empty异常
# 所以更常用的方法是先判断一个队列是否为空，如果不为空则取值


print(q.empty())
# 队列的操作：存--put()  取--get()
q.put('page1')
q.put('page2')
q.put('page3')

print(q.empty())
# 判断队列是否已经满了
print(q.full())

q1 = Queue(3)  # 在创建队列时，指定队列大小（表示该队列最多能存多少个元素）
q1.put('1')
q1.put('1')
q1.put('1')
print(q1.full())

q2 = Queue(3)
q2.put('1')
q2.put('2')
q2.put('3')
value = q2.get()  # 遵循的原则是：先进先出
print(value)
print(q2.full())

# 存数据---阻塞
q3 = Queue(3)
q3.put(1)
q3.put(2)
q3.put(3)
# q3.put(4)#如果队列已经满了，等着（阻塞），一直等到队列腾出空间，然后把值存入到队列当中。

# 取数据--阻塞
q4 = Queue(3)
q4.put(1)
value = q4.get()  # 1,此时队列为空
print('q4:', value)
# value = q4.get()#阻塞，直到队列当中有新值的时候，取出，结束阻塞。

# 非阻塞
q5 = Queue(3)
q5.put(1)

# 1.取
print('q5.qsize:', q5.qsize())  # 当前队列当中的元素个数
# 方法1：
# while not q5.empty():
#     value2 = q5.get(block=False)#block为Ture，表示阻塞，否则为非阻塞。非阻塞就是“强取”
#     print('q5：',value2)
# 方法2：
while q5.qsize() > 0:
    value2 = q5.get(block=False)
    print('q5：', value2)

print('q5.qsize:', q5.qsize())
# 存
q6 = Queue(3)

# 方法1：
# print(q6.maxsize)#得到队列最大容量
# i = 0
# while i<q6.maxsize:
#     q6.put(i)
#     i+=1

# 方法2：
while not q6.full():
    q6.put(1, block=False)  # 非阻塞

'''------------------------------其它的属性和方法-----------------------------'''
q7 = Queue(3)
# q7.get(block=False)
print(time.time())
try:
    q7.get(timeout=2)  # 阻塞时长
except:
    pass
print(time.time())

q8 = Queue(3)
# q8.get_nowait()#强取

'''------------------------------优先级队列-----------------------------'''
q = PriorityQueue()

# 格式：q.put((数字,值))
# 特点：数字越小，优先级越高
q.put((1, 'lori'))
q.put((-1, 'Jseon'))
q.put((10, 'King'))

i = 0
while i < q.qsize():
    print(q.get())

import heapq


class PriorityQueue(object):
    def __init__(self):
        self._queue = []  # 创建一个空列表用于存放队列
        self._index = 0  # 指针用于记录push的次序

    def push(self, item, priority):
        """队列由（priority, index, item)形式的元祖构成"""
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]  # 返回拥有最高优先级的项


class Item(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item: {!r}'.format(self.name)


if __name__ == '__main__':
    q = PriorityQueue()
    q.push(Item('foo'), 5)
    q.push(Item('bar'), 1)
    q.push(Item('spam'), 3)
    q.push(Item('grok'), 1)
    for i in range(4):
        print(q._queue)
        print(q.pop())


