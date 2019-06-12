
'''

问题

怎样实现一个按优先级排序的队列？ 并且在这个队列上面每次 pop 操作总是返回优先级最高的那个元素
解决方案

下面的类利用 heapq 模块实现了一个简单的优先级队列：

'''

import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, prioriry):
        heapq.heappush(self._queue,(-prioriry, self._index, item))
        self._index += 1
    
    def pop(self):
        return heapq.heappop(self._queue)[-1]


#堆排序
def heapsort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]
print(heapsort([1,3,5,7,9,2,4,6,8,0]))