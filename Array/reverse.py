def reverse(x: int) -> int:
    """
    在python语言中，如果要向x%10(x<0)仍为负数，需要使用x%-10
    x//10(x<0)会得出偏左的负数结果，想要偏0的负数结果使用int(x/10)
    :param x:
    :return:
    """
    INTMIN = int(-2 ** 31/10)
    INTMAX = (2 ** 31 - 1) // 10
    rev = 0
    while x:
        pop = x % 10 if x > 0 else x % -10
        x = int(x / 10)
        if rev > INTMAX or (rev == INTMAX and pop > 7):
            return 0
        if rev < INTMIN or (rev == INTMIN and pop < -8):
            return 0
        rev = rev * 10 + pop
    return rev


print(reverse(1534236469))
