def hanoi(n, start, destination, via):
    if n <= 1:
        return 1
    count = 0
    count += hanoi(n - 1, start, via, destination)
    count += 1
    count += hanoi(n - 1, via, destination, start)

    return count


if __name__ == "__main__":
    n, start, destination, via = 3, 1, 3, 2
    total_count = hanoi(n, start, destination, via)
    print(total_count)
