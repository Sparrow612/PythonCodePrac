from typing import List


# 未完成
def checkPossibility(nums: List[int]) -> bool:
    lower = nums[0]
    for i in range(len(nums) - 1):
        if nums[i + 1] < nums[i]:
            if not err:
                err = True
            else:
                return False
    return True
