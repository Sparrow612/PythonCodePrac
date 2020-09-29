from typing import List

from Tree.tree_node import TreeNode


# 递归算法解决，用脚都能实现想
def postorderTraversal(root: TreeNode) -> List[int]:
    def postorder(root):
        if not root: return
        postorder(root.left)
        postorder(root.right)
        res.append(root.val)

    res = list()
    postorder(root)
    return res


# 迭代算法实现后序遍历
def postorder_with_iter(root: TreeNode) -> List[int]:
    if not root: return list()

    res = list()
    stack = list()
    prev = None

    while root or stack:
        # 首先，把一路向左子树遍历
        # 相当于上面的 postorder(root.left)
        while root:
            stack.append(root)
            root = root.left
        # 然后，挨个弹出root，压入右子树
        root = stack.pop()
        # 如果没有右子树，那么直接输出根结点
        # root.right == prev 表示当前root的右子树遍历完成
        if not root.right or root.right == prev:
            res.append(root.val)
            prev = root
            root = None
        else:
            # 相当于上面的 postorder(root.right)
            stack.append(root)
            root = root.right
    return res


root = TreeNode(1)
r = TreeNode(2)
l = TreeNode(3)
root.right = r
r.left = l
print(postorder_with_iter(root))
