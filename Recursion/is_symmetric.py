class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isSymmetric(root: TreeNode) -> bool:
    def check(left: TreeNode, rignt: TreeNode) -> bool:
        if not left and not rignt: return True
        if not left or not rignt: return False
        return left.val == rignt.val and check(left.left, rignt.right) and check(left.right, rignt.left)
    if not root: return True
    return check(root.left, root.right)