"""
leetcode 2021.2.14 765 情侣牵手

法一：
看了一下题解，大多采用并查集思想，那么就来试一试
"""
from typing import List

p = [0] * 70


def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]


def union(a, b):
    p[find(a)] = p[find(b)]


def minSwapsCouples_DSU(row):
    """
    两对情侣互相错位，交换一次
    三对情侣互相错位，交换2次
    k对情侣互相错位，交换k-1次

    互相错位的情侣对看成一个环，有一个环就要-1，我们只需找到n/2对情侣中有几个这样的环即可
    :param row:
    :return:
    """
    n = len(row)
    m = n // 2  # 情侣的对数
    for i in range(m):
        p[i] = i
    for i in range(0, n, 2):
        union(row[i] // 2, row[i + 1] // 2)
    cnt = 0
    for i in range(m):
        if i == p[i]: cnt += 1
    return m - cnt


def minSwapsCouples(row: List[int]) -> int:
    """
    法二：记录一位牛人的神奇解法，有点像贪心算法
    """
    N = len(row)
    pos = {val: i for i, val in enumerate(row)}
    ans = 0
    for i in range(1, N, 2):
        while row[i - 1] != row[i] ^ 1:
            index = pos[row[i] ^ 1] ^ 1
            row[i], row[index] = row[index], row[i]
            ans += 1
    return ans
