from typing import List
from Tree.tree_node import TreeNode

"""
算法解释：

完全覆盖的方法
1. root放摄像头，两棵子树被覆盖即可
2. root不放摄像头，两棵子树之一必须放摄像头，且各自被覆盖

状态 a: root必须放置摄像头的情况下，覆盖整棵树需要的最小摄像头数目。
状态 b: 覆盖整棵树需要的最小摄像头数目，无论root是否放置摄像头。
状态 c: 覆盖两棵子树需要的最小摄像头数目，无论节点root本身是否被监控到。

a = lc + rc + 1
b = min(a, min(la + rb, lb + ra))
c = min(b, lb + rb)
a ≥ b ≥ c
"""


def minCameraCover(root: TreeNode) -> int:
    def dfs(root: TreeNode) -> List[int]:
        if not root:
            return [float('inf'), 0, 0]
        la, lb, lc = dfs(root.left)
        ra, rb, rc = dfs(root.right)
        a = lc + rc + 1
        b = min(a, min(la + rb, lb + ra))
        c = min(b, lb + rb)
        return [a, b, c]
    a, b, c = dfs(root)
    return b
