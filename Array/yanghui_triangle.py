"""
leetcode 杨辉三角2
"""
from typing import List


def getRow(rowIndex: int) -> List[int]:
    arr = [1]
    for row in range(1, rowIndex + 1):
        arr.append(0)
        arr_copy = arr.copy()
        for index in range(1, row + 1):
            arr_copy[index] = arr[index - 1] + arr[index]
        arr = arr_copy
    return arr


print(getRow(4))
