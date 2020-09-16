from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    result = list()
    permute_with_list(nums, result, 0, len(nums) - 1)
    return result


def permute_with_list(nums: List[int], res, low, high):
    if low == high:
        res.append(nums[:])
        return
    for i in range(low, high + 1):
        nums[low], nums[i] = nums[i], nums[low]
        permute_with_list(nums, res, low + 1, high)
        nums[low], nums[i] = nums[i], nums[low]


if __name__ == '__main__':
    res = [1, 2, 3]
    print(permute(res))
