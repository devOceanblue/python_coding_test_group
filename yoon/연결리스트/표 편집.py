def solution(n, k, cmd):
    deleted = []
    temp = ["O" for _ in range(n)]
    for c in cmd:
        c = c.split(" ")
        if c[0] == "U":
            num = int(c[1])
            while num > 0:
                if temp[k - 1] == "O":
                    num -= 1
                k -= 1
                k %= n
        elif c[0] == "D":
            num = int(c[1])
            while num > 0:
                if temp[(k + 1) % n] == "O":
                    num -= 1
                k += 1
                k %= n
        elif c[0] == "C":
            num = 1
            temp[k] = "X"
            deleted.append(k)
            if k == n - 1:
                while num > 0:
                    if temp[(k - 1) % n] == "O":
                        num -= 1
                k -= 1
                k %= n
            else:
                while num > 0:
                    if temp[(k + 1) % n] == "O":
                        num -= 1
                k += 1
                k %= n
        elif c[0] == "Z":
            pointer = deleted.pop()
            temp[pointer] = "O"
    return "".join(temp)


if __name__ == "__main__":
    print(solution(3, 1, ["D 12", "C", "C", "Z"]))
