from typing import List


def diff_btw_time(pre, aft):
    res = 0
    pre = [int(n) for n in pre.split(':')]
    aft = [int(n) for n in aft.split(':')]
    if aft[1] > pre[1]:
        res += aft[1] - pre[1]
        if aft[0] > pre[0]:
            res += 60 * (aft[0] - pre[0])
    else:
        aft[0] -= 1
        res += (aft[1] + 60 - pre[1]) + 60 * (aft[0] - pre[0])
    return res


def check(time_list):
    time_list.sort()
    n = len(time_list)
    for i in range(n - 2):
        if diff_btw_time(time_list[i], time_list[i + 1]) + diff_btw_time(time_list[i + 1], time_list[i + 2]) <= 60:
            return time_list[i], time_list[i + 1], time_list[i + 2]
    return None


class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        n = len(keyName)
        repo = {}
        times = {}
        result = {}
        for i in range(n):
            name = keyName[i]
            if name not in repo:
                repo[name] = 1
                times[name] = [keyTime[i]]
            else:
                repo[name] += 1
                times[name].append(keyTime[i])
                if repo[name] >= 3:
                    res = check(times[name])
                    if res: result[name] = res
        result = list(result.items())
        result.sort(key=lambda x: x[0])
        return [x[0] for x in result]


if __name__ == '__main__':
    s = Solution()
    keyn = ["daniel", "daniel", "daniel", "luis", "luis", "luis", "luis"]
    keyt = ["10:00", "10:40", "11:00", "09:00", "11:00", "13:00", "15:00"]
    print(s.alertNames(keyn, keyt))
