"""
Leetcode 703 数据流中的第K大元素

设计一个找到数据流中第 k 大元素的类（class）。注意是排序后的第 k 大元素，不是第 k 个不同的元素。

请实现 KthLargest类：

KthLargest(int k, int[] nums) 使用整数 k 和整数流 nums 初始化对象。
int add(int val) 将 val 插入数据流 nums 后，返回当前数据流中第 k 大的元素。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-largest-element-in-a-stream
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


解题思路：
使用堆（优先级队列）数据结构解决
1. 直接使用python的heapq模块
2. 手写堆数据结构
"""
from typing import List
import heapq
import math


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.queue = [0] * k
        heapq.heapify(self.queue)

    def add(self, val: int) -> int:
        heapq.heappush(self.queue, val)
        while len(self.queue) > self.k:
            heapq.heappop(self.queue)
        return self.queue[0]


"""
堆是一种很重要的数据结构，光会调库是不够的，还需要实现一下加深理解
这里实现的是小根堆
"""


class MyHeap:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = [0] * k
        self.count = 0  # 堆的元素个数
        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        """
        只有在两种情况下才需要真正把值加入堆
        1. 堆元素数量小于k
        2. 堆的根节点（最小元素）小于加入的元素
        :param val: 要插入的值
        :return: 根节点的值，也就是堆中的最小元素
        """
        if self.count < self.k:
            self.heap[self.count] = val
            self.__up(self.count)
            self.count += 1
        elif self.heap[0] < val:
            # 插入值大于根节点，替换并下移
            self.heap[0] = val
            self.__down(0)
        return self.heap[0]

    def __up(self, node):
        while (math.ceil(node / 2) - 1) >= 0 and self.heap[math.ceil(node / 2) - 1] > self.heap[node]:
            self.heap[node], self.heap[math.ceil(node / 2) - 1] = self.heap[math.ceil(node / 2) - 1], self.heap[node]
            node = math.ceil(node / 2) - 1

    def __down(self, node):
        """
        初始的堆元素值为-1，所以只需要检查元素索引是否小于count即可确认后代是否存在
        :param node:
        :return:
        """
        t = node
        if 2 * node + 1 < self.count and self.heap[2 * node + 1] < self.heap[t]:
            t = 2 * node + 1
        if 2 * node + 2 < self.count and self.heap[2 * node + 2] < self.heap[t]:
            t = 2 * node + 2
        if t != node:
            self.heap[node], self.heap[t] = self.heap[t], self.heap[node]
            self.__down(t)


myheap = MyHeap(3, [4, 5, 8, 2])
myheap.add(3)
myheap.add(5)
myheap.add(10)
print(myheap.heap)
