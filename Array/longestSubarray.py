"""
Leetcode 1438 绝对差不超过限制的最长连续子数组
给你一个整数数组 nums ，和一个表示限制的整数 limit，请你返回最长连续子数组的长度，该子数组中的任意两个元素之间的绝对差必须小于或者等于 limit 。

如果不存在满足条件的子数组，则返回 0 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
import sortedcontainers


def longestSubarray(nums, limit) -> int:
    """
    方法一思路上是没问题的，但是时间复杂度太高了，需要改进
    :param nums:
    :param limit:
    :return:
    """
    left, right = 0, -1
    n = len(nums)
    queMax, queMin = 0, 10 ** 9
    maxLen = 0
    for i in range(n):
        right += 1
        queMax = max(queMax, nums[right])
        queMin = min(queMin, nums[right])
        if queMax - queMin <= limit:
            maxLen = max(maxLen, right - left + 1)
        while queMax - queMin > limit:
            left += 1
            queMin = min(nums[left:right + 1])
            queMax = max(nums[left:right + 1])
    maxLen = max(maxLen, right - left + 1)
    return maxLen


def longestSubarray_v2(nums, limit) -> int:
    """
    我的想法是用字典来记录子数组中每个元素的个数，这样更新时就可以更方便避免遍历寻找最值
    只有最后和最值相同的最后一个元素离开，最值才需要更新
    但是这种解法还是没起到效果，复杂度仍然太高
    :param nums:
    :param limit:
    :return:
    """
    left, right = 0, -1
    n = len(nums)
    queMax, queMin = 0, 10 ** 9
    curVals = collections.defaultdict(int)
    maxLen = 0
    for i in range(n):
        right += 1
        curVals[nums[right]] += 1
        queMax = max(queMax, nums[right])
        queMin = min(queMin, nums[right])
        if queMax - queMin <= limit:
            maxLen = max(maxLen, right - left + 1)
        while queMax - queMin > limit:
            curVals[nums[left]] -= 1
            left += 1
            while curVals[queMin] == 0:
                queMin += 1
            while curVals[queMax] == 0:
                queMax -= 1
    maxLen = max(maxLen, right - left + 1)
    return maxLen


def longestSubarray_v3(nums, limit):
    """
    居然是调库的过了。。
    :param nums:
    :param limit:
    :return:
    """
    s = sortedcontainers.SortedList()
    n = len(nums)
    left, right = 0, 0
    res = 0
    for i in range(n):
        s.add(nums[right])
        while s[-1] - s[0] > limit:
            s.remove(nums[left])
            left += 1
        res = max(res, right - left + 1)
        right += 1
    return res


def longestSubarray_v4(nums, limit):
    """
    滑动窗口+单调队列
    单调递减的queMax
    单调递增的queMin
    :param nums:
    :param limit:
    :return:
    """
    left, right = 0, 0
    queMax, queMin = collections.deque(), collections.deque()
    res = 0
    n = len(nums)
    for i in range(n):
        while queMax and queMax[-1] < nums[right]:
            queMax.pop()
        while queMin and queMin[-1] > nums[right]:
            queMin.pop()

        queMin.append(nums[right])
        queMax.append(nums[right])
        
        while queMax[0] - queMin[0] > limit:
            if nums[left] == queMin[0]:
                queMin.popleft()
            if nums[left] == queMax[0]:
                queMax.popleft()
            left += 1
        res = max(res, right - left + 1)
        right += 1
    return res


print(longestSubarray_v3([10, 1, 2, 4, 7, 2], 5))
