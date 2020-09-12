from typing import List


def combinationSum3(k: int, n: int) -> List[List[int]]:
    pool = []
    for i in range(9):
        pool.append(i + 1)
    return combinationSum_with_pool(k, n, pool)


def combinationSum_with_pool(k, n, pool) -> List[List[int]]:
    res = []
    if k == 1:
        tmp = []
        if n in pool:
            tmp.append(n)
            res.append(tmp)
        return res
    for i in range(len(pool)):
        if pool[i] >= n / 2: break
        tmp = [pool[i]]
        pool.pop(i)
        for s in combinationSum_with_pool(k - 1, n - tmp[0], pool):
            tmp.extend(s)
            v = sorted(tmp)
            if v not in res: res.append(v)
            tmp = tmp[0:1]
        pool.insert(i, tmp[0])  # 恢复取数池
    return res


if __name__ == '__main__':
    print(combinationSum3(3, 9))

# 过是过了，但是还是想想改进方案吧，因为运行速度有点感人……
