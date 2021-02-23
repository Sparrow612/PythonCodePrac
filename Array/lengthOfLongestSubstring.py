def lengthOfLongestSubstring(s: str) -> int:
    if len(s) == 0: return 0
    maxlen, curlen = 0, 0
    lookup = set()
    left = 0
    for c in s:
        while c in lookup:
            maxlen = max(maxlen, curlen)
            lookup.remove(s[left])
            curlen -= 1
            left += 1
        lookup.add(c)
        curlen += 1
    maxlen = max(maxlen, curlen)
    return maxlen


print(lengthOfLongestSubstring(" "))
