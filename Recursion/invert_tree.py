class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def invertTree(root: TreeNode) -> TreeNode:
    if not root: return root
    invertTree(root.left)
    invertTree(root.right)
    root.left, root.right = root.right, root.left
    return root
