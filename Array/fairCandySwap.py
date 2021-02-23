"""
leetcode 888 公平的糖果交换

这道题就是简单的数学题

sumA - x + y = sumB + x - y
x = y + (sumA - sumB)/2
"""
from typing import List


def fairCandySwap(A: List[int], B: List[int]) -> List[int]:
    """
    最简单的方式，暴力查找
    :param A:
    :param B:
    :return:
    """
    sumA = sum(A)
    sumB = sum(B)
    gap = int((sumA - sumB) / 2)
    for x in A:
        if x - gap in B:
            return [x, x - gap]
    return []


def fairCandySwap_ver2(A: List[int], B: List[int]) -> List[int]:
    """
    在上一种方法的基础上，使用哈希表优化时间复杂度
    :param A:
    :param B:
    :return:
    """
    sumA = sum(A)
    sumB = sum(B)
    setB = set(B)
    gap = (sumA - sumB) // 2
    for x in A:
        if x - gap in setB:
            return [x, x - gap]
    return []


def fairCandySwap_ver3(A: List[int], B: List[int]) -> List[int]:
    """
    在法一的基础上，使用二分查找进行优化
    :param A:
    :param B:
    :return:
    """
    sumA = sum(A)
    sumB = sum(B)
    gap = (sumA - sumB) // 2
    B.sort()  # 先排好序，才能使用二分查找
    for x in A:
        l, r = 0, len(B) - 1
        while 0 <= l <= r < len(B):
            mid = (l + r) // 2
            if B[mid] == x - gap:
                return [x, x - gap]
            elif B[mid] > x - gap:
                r = mid - 1
            else: l = mid + 1
    return []