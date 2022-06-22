n = int(input())

tile = [0, 1, 2, 3]

for i in range(4, n + 1):
    tile.append(tile[i - 1] + tile[i - 2])

print(tile[n] % 10007)