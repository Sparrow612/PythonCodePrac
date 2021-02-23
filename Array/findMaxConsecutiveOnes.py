from typing import List


def findMaxConsecutiveOnes(nums: List[int]) -> int:
    idx = 0
    maxOnes = 0
    curOnes = 0
    while idx < len(nums):
        if nums[idx] == 1:
            curOnes += 1
        else:
            maxOnes = max(maxOnes, curOnes)
            curOnes = 0
        idx += 1
    maxOnes = max(maxOnes, curOnes)
    return maxOnes


print(findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
