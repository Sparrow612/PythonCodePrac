from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def getAvg(p):
    s = 0.0
    for n in p:
        s += n.val
    return s/len(p)


def averageOfLevels(root: TreeNode) -> List[float]:
    res = [root.val]
    pool = []
    if root.left: pool.append(root.left)
    if root.right: pool.append(root.right)
    while len(pool) > 0:
        res.append(getAvg(pool))
        l = len(pool)
        for i in range(l):
            if pool[i].left: pool.append(pool[i].left)
            if pool[i].right: pool.append(pool[i].right)
        for i in range(l):
            pool.pop(0)
    return res


if __name__ == '__main__':
    t1 = TreeNode(15)
    t2 = TreeNode(7)
    t3 = TreeNode(20)
    t3.left = t1
    t3.right = t2
    t4 = TreeNode(9)
    t5 = TreeNode(3)
    t5.left = t4
    t5.right = t3
    print(averageOfLevels(t5))
