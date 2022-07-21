n = 10
r = 511
c = 511
num = -1


def recursive(x, y, n):
    global num

    if n == 2:
        for i in range(x, x + n):
            for j in range(y, y + n):
                num += 1
                if i == r and j == c:
                    print(num)
                    exit(0)
        return

    for i in range(x, x + n, n // 2):
        for j in range(y, y + n, n // 2):
            recursive(i, j, n // 2)


if __name__ == "__main__":
    print(recursive(0, 0, 2 ** n))
