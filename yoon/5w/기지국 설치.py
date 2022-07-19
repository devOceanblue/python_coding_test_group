from math import ceil


def solution(n, stations, w):
    answer = 0
    width = 2 * w + 1

    start = 1
    for s in stations:
        answer += max(ceil((s - w - start) / width), 0)
        start = s + w + 1

    if n >= start:
        answer += ceil((n - start + 1) / width)

    return answer


if __name__ == "__main__":
    assert solution(n=11, stations=[4, 11], w=1) == 3
