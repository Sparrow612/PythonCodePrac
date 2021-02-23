"""
给定一个由若干 0 和 1 组成的数组 A，我们最多可以将 K 个值从 0 变成 1 。

返回仅包含 1 的最长（连续）子数组的长度。

我们转换一下思路：找到最长的子数组，至多包含K个0
"""
from typing import List


def longestOnes(A: List[int], K: int) -> int:
    n = len(A)
    left, right = 0, -1
    zeroNum = 0
    maxLen, curLen = 0, 0
    for i in range(n):
        right += 1
        curLen += 1
        if A[right] == 0:
            zeroNum += 1
        if zeroNum > K:
            maxLen = max(curLen - 1, maxLen)
        while zeroNum > K:
            if A[left] == 0:
                zeroNum -= 1
            left += 1
            curLen -= 1
    maxLen = max(curLen, maxLen)
    return maxLen


print(longestOnes([0, 0, 0, 1], 4))
