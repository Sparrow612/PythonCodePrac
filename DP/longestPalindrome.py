"""
leetcode 5 最长回文子串
"""


def longestPalindrome(s: str) -> str:
    """
    动态规划解法：
    dp(i, j)表示s[i:j+1]是否为回文串
    1. 状态转移
        dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
    2. 边界值
        dp[i][i] = True
        dp[i][i+1] = s[i] == s[j+1]
    :param s:
    :return:
    """
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    ans = ''
    for l in range(n):
        for i in range(0, n - l):
            j = i + l
            if l == 0:
                dp[i][j] = True
            elif l == 1:
                dp[i][j] = s[i] == s[j]
            else: dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
            if dp[i][j] and l + 1 > len(ans):
                ans = s[i:j + 1]
    return ans
