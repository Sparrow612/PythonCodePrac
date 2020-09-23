from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def inorderTraversal(root: TreeNode) -> List[int]:
    res = list()
    inorderTraversal_with_pool(root, res)
    return res


def inorderTraversal_with_pool(root: TreeNode, res_pool):
    if not root: return
    if root.left: inorderTraversal_with_pool(root.left, res_pool)
    res_pool.append(root.val)
    if root.right: inorderTraversal_with_pool(root.right, res_pool)
