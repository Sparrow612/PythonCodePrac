"""
leetcode 4 寻找两个正序数组的中位数
"""
from typing import List


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    """
    我的第一个思路很简单，先把两个数组合并，然后直接取中位数即可
    :param nums1:
    :param nums2:
    :return:
    """
    nums = []
    cur1, cur2 = 0, 0
    n1, n2 = len(nums1), len(nums2)
    while cur1 < n1 and cur2 < n2:
        if nums1[cur1] < nums2[cur2]:
            nums.append(nums1[cur1])
            cur1 += 1
        else:
            nums.append(nums2[cur2])
            cur2 += 1
    # 合并完还剩个尾巴
    if cur1 < n1:
        for i in range(cur1, n1):
            nums.append(nums1[i])
    elif cur2 < n2:
        for i in range(cur2, n2):
            nums.append(nums2[i])
    # 数组合并完成
    n = n1 + n2
    if n % 2 == 1:
        mid = nums[(n - 1) // 2]
    else:
        mid = (nums[(n - 1) // 2] + nums[(n - 1) // 2 + 1]) / 2
    return mid


print(findMedianSortedArrays([1, 3], [2]))
