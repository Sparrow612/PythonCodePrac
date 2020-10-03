class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    res = ListNode()
    cur = res
    p, q = l1, l2
    carry = 0
    while p or q:
        x = p.val if p else 0
        y = q.val if q else 0  # 这里的写法非常好
        s = x + y + carry
        carry = s // 10
        s %= 10
        cur.next = ListNode(s)
        cur = cur.next
        if p: p = p.next
        if q: q = q.next
    if carry > 0:
        cur.next = ListNode(carry)
    return res.next
