from typing import List


def subset(nums: List[int]) -> List[List[int]]:
    cur = 0
    n = len(nums)
    subsets = []
    while cur < 2 ** n:
        tmp = cur
        res = []
        ptr = 0
        while tmp:
            if tmp & 1: res.append(nums[ptr])
            ptr += 1
            tmp >>= 1
        cur += 1
        subsets.append(res)
    return subsets


# bitmap算法的确巧妙，但是太慢了，试试别的，比如递归？
if __name__ == '__main__':
    print(subset([1, 2, 3]))