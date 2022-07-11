from collections import defaultdict


def solution(gems):
    l = 0
    r = 0
    e = len(gems)
    cur_gems = defaultdict(int)
    cur_gems[gems[0]] = 1
    kind = set(gems)
    cur = [0, e - 1]

    while l < e and r < e:
        if len(cur_gems) < len(kind):
            r += 1
            if r == e:
                break
            cur_gems[gems[r]] += 1
        else:
            if r - l < cur[1] - cur[0]:
                cur = [l, r]
            if cur_gems[gems[l]] == 1:
                del cur_gems[gems[l]]
            else:
                cur_gems[gems[l]] -= 1
            l += 1
    return [cur[0] + 1, cur[1] + 1]


if __name__ == "__main__":
    assert (solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"])) == [1, 5]
