class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseKGroup(head: ListNode, k: int) -> ListNode:
    bfr, nxt = None, head
    res = None
    stk = []
    while nxt:
        for i in range(k):
            if not nxt:
                if not res:
                    res = head  # list个数小于k
                else:
                    bfr.next = stk[0]  # 前面一节要接上
                return res
            stk.append(nxt)
            nxt = nxt.next
        for i in range(k):
            if not res:
                res = stk[-1]
                bfr = res
            else:
                bfr.next = stk[-1]
                bfr = bfr.next
            stk.pop(-1)
        bfr.next = None  # 如果不加这一行，[1,2],2就会形成死循环
    return res


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)

if __name__ == '__main__':
    a.next = b
    res = reverseKGroup(a, 2)
    for i in range(2):
        print(res.val)
        res = res.next
