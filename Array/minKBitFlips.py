"""
2020.2.18 每日一题
当天尝试失败，这题目太阴间了。。。
"""
import collections
from typing import List


def minKBitFlips(A: List[int], K: int) -> int:
    """
    滑动窗口解法
    :param A:
    :param K:
    :return:
    """
    que = collections.deque()
    n = len(A)
    res = 0
    for i in range(n):
        if len(que) and i >= que[0] + K:
            que.popleft()
        if len(que) % 2 == A[i]:
            """
            len(que)表示当前位置的数被翻转的次数
            如果A[i]为1，被翻转奇数次为0，需要翻转
            如果A[i]为0，被翻转偶数次为0，需要翻转
            """
            if i + K - 1 >= n: return -1
            que.append(i)
            res += 1
    return res


print(minKBitFlips([0, 1, 1, 1, 0, 0], 3))
