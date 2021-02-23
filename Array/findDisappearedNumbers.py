from typing import List

"""
Leetcode 2021.2.13
找到所有数组中消失的数字

解法：遍历数组，遇到数x将nums[x-1]加n
最后，数组中不大于n的num[i]说明原数组中没有出现i+1
"""


def findDisappearedNumbers(nums: List[int]) -> List[int]:
    n = len(nums)
    result = []
    for x in nums:
        x = x % n
        nums[x - 1] += n
    for i in range(n):
        if nums[i] <= n:
            result.append(i+1)
    return result