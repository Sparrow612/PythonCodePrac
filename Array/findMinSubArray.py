"""
leetcode 697 数组的度
给定一个非空且只包含非负数的整数数组 nums，数组的度的定义是指数组里任一元素出现频数的最大值。

你的任务是在 nums 中找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/degree-of-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from typing import List


def findShortestSubArray(nums: List[int]) -> int:
    """
    一个子数组的度要和原数组一样，一定要包含所有的最高频元素，也就是从第一个出现的最高频元素到最后一个最高频元素（保存左右边界）
    """
    n = len(nums)
    que = []
    ori = collections.defaultdict(int)
    left = collections.defaultdict(int)
    right = collections.defaultdict(int)
    degree = 0
    for i in range(n):
        if left[nums[i]]:
            right[nums[i]] = i + 1
        else:
            left[nums[i]] = i + 1
        ori[nums[i]] += 1
        degree = max(degree, ori[nums[i]])
    if degree == 1: return 1
    for k, v in ori.items():
        if v == degree:
            que.append(k)
    minLen = 50001
    for k in que:
        minLen = min(minLen, right[k] - left[k] + 1)
    return minLen


print(findShortestSubArray([1]))
