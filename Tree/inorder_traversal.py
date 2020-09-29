from typing import List

from Tree.tree_node import TreeNode


# 递归算法解决，用脚都能实现想
def inorderTraversal(root: TreeNode) -> List[int]:
    def inorder(root):
        if not root: return
        inorder(root.left)
        res.append(root.val)
        inorder(root.right)

    res = list()
    inorder(root)
    return res


def inorder_with_iter(root):
    if not root: return list()

    res = list()
    stack = list()

    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        res.append(root.val)
        if root.right:
            root = root.right
        else:
            root = None
    return res


root = TreeNode(1)
r = TreeNode(2)
l = TreeNode(3)
root.right = r
r.left = l
print(inorder_with_iter(root))
