from typing import List


def permuteUnique(nums: List[int]) -> List[List[int]]:
    result = list()
    permuteUnique_with_list(nums, result, 0, len(nums) - 1)
    return result


def permuteUnique_with_list(nums: List[int], res, low, high):
    if low == high:
        if nums not in res:
            res.append(nums[:])
        return
    for i in range(low, high + 1):
        nums[low], nums[i] = nums[i], nums[low]
        permuteUnique_with_list(nums, res, low + 1, high)
        nums[low], nums[i] = nums[i], nums[low]


if __name__ == '__main__':
    res = [1, 1, 2]
    print(permuteUnique(res))
