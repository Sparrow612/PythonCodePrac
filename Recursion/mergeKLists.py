from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge2Lists(lista, listb):
    head = ListNode()
    cur = head
    if not lista or not listb:
        return lista if lista else listb
    while lista and listb:
        if lista.val < listb.val:
            cur.next = lista
            lista = lista.next
        else:
            cur.next = listb
            listb = listb.next
        cur = cur.next
    cur.next = lista if lista else listb
    return head.next


def merge(lists, l, r):
    if l > r: return None
    if l == r: return lists[l]
    mid = (l + r) // 2
    return merge2Lists(merge(lists, l, mid), merge(lists, mid + 1, r))


def mergeKLists(lists: List[ListNode]) -> ListNode:
    return merge(lists, 0, len(lists) - 1)


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)