class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
本题中要求我们将每个节点的值修改为原来的节点值加上所有大于它的节点值之和。这样我们只需要反序中序遍历该二叉搜索树，记录过程中的节点值之和，并不断更新当前遍历到的节点的节点值，即可得到题目要求的累加树。
关键词：反序中序遍历
中序遍历是从小到大，那么从大到小反过来即可
PS：这题是看答案看来的
"""

sum_of_val = 0  # 遍历和


def convertBST(root: TreeNode) -> TreeNode:
    global sum_of_val
    if root:
        convertBST(root.right)
        sum_of_val += root.val
        root.val = sum_of_val
        convertBST(root.left)
    return root


def another_convert_bst(root):
    """
    :param root: TreeNode
    :return: root
    这段代码思路和上面一样，只不过换了一种实现方式
    """
    def dfs(root: TreeNode):
        nonlocal total
        if root:
            dfs(root.right)
            total += root.val
            root.val = total
            dfs(root.left)

    total = 0
    dfs(root)
    return root


if __name__ == '__main__':
    root = TreeNode(2)
    left = TreeNode(1)
    right = TreeNode(3)
    # ll = TreeNode(-4)
    # lr = TreeNode(1)
    # left.left = ll
    # left.right = lr
    root.left = left
    root.right = right
    root = convertBST(root)
    print(root.val)
    print(root.left.val)
    print(root.right.val)
    # print(root.left.left.val)
    # print(root.left.right.val)
