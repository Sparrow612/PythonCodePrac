from queue import Queue
from typing import List


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def connect(root: Node) -> Node:
    def bfs(layer) -> None:
        while layer.qsize():
            n = layer.qsize()
            cur = 0
            beforeNode = layer.get()
            while cur < n - 1:
                if beforeNode.left: layer.put(beforeNode.left)
                if beforeNode.right: layer.put(beforeNode.right)
                beforeNode.next = layer.get()
                beforeNode = beforeNode.next
                cur += 1
            beforeNode.next = None
            if beforeNode.left: layer.put(beforeNode.left)
            if beforeNode.right: layer.put(beforeNode.right)
    layer = Queue()
    if root:
        layer.put(root)
        bfs(layer)
    return root


if __name__ == '__main__':
    root = Node(1)
    n1 = Node(2)
    n2 = Node(3)
    n3 = Node(4)
    n4 = Node(5)
    n5 = Node(7)
    root.left  = n1
    root.right = n2
    n1.left = n3
    n1.right = n4
    n2.right = n5
    connect(root)
