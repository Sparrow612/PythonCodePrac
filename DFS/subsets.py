from typing import List


def subset_with_limits(nums, left, right, pre, res):
    if left == right:
        tmp = []
        for i in range(len(nums)):
            if pre[i]: tmp.append(nums[i])
        res.append(tmp)
        return
    subset_with_limits(nums, left + 1, right, pre, res)
    pre[left] = 1
    subset_with_limits(nums, left + 1, right, pre, res)
    pre[left] = 0  # 退位


def subset(nums: List[int]) -> List[List[int]]:
    result = list()
    n = len(nums)
    subset_with_limits(nums, 0, n, [0] * n, result)
    return result


# 深度优先搜索方法比原来的好了很多
if __name__ == '__main__':
    print(subset([1, 2, 3]))
