"""
leetcode 566 重塑矩阵
"""
from typing import List


def matrixReshape(nums: List[List[int]], r: int, c: int) -> List[List[int]]:
    m, n = len(nums), len(nums[0])  # 原矩阵的行数和列数
    if m * n != r * c: return nums
    result = [[0] * c for _ in range(r)]
    cur = 0
    while cur < r * c:
        i1, j1 = cur // c, cur % c
        i2, j2 = cur // n, cur % n
        result[i1][j1] = nums[i2][j2]
        cur += 1
    return result


print(matrixReshape([[1, 2], [3, 4]], 1, 4))
