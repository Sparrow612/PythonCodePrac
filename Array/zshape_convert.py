"""
leetcode 6 Z字形变换
"""


def convert(s: str, numRows: int) -> str:
    """
    不要被题目的Z所迷惑，按照顺序走，用一组列表将走过的字符挨个加入对应列表中即可（千万不要傻乎乎的排成Z）
    :param s:
    :param numRows:
    :return:
    """
    if numRows == 1: return s
    res = [[] for _ in range(min(len(s), numRows))]
    resultStr = ''
    curRow = 0
    goingDown = False
    for c in s:
        res[curRow].append(c)
        if curRow == 0 or curRow == numRows - 1: goingDown = not goingDown
        curRow += 1 if goingDown else -1
    for r in res:
        for c in r:
            resultStr += c
    return resultStr
