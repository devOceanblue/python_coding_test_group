n = int(input())
array = list(map(int, input().split()))
sArray = sorted(list(set(array)))
dic ={item : idx for idx, item in enumerate(sArray)}
for item in array:
    print(dic[item], end = ' ')