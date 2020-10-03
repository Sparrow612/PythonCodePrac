from typing import List

from Tree.tree_node import TreeNode


def buildTree(preorder: List[int], inorder: List[int]) -> TreeNode:
    if not preorder: return None
    root = TreeNode(preorder[0])
    pos = inorder.index(preorder[0])
    root.left = buildTree(preorder[1:1+pos], inorder[:pos])
    root.right = buildTree(preorder[pos+1:], inorder[1+pos:])
    return root


def buildTree_another(inorder: List[int], postorder: List[int]) -> TreeNode:
    if not inorder: return None
    root = TreeNode(postorder[-1])
    pos = inorder.index(postorder[-1])
    root.left = buildTree(inorder[:pos], postorder[:pos])
    root.right = buildTree(inorder[1 + pos:], postorder[pos:-1])
    return root