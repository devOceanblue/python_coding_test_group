def soultion(n):
    array = list(map(int, input().split()))
    sArray = sorted(list(set(array)))
    dic ={item : idx for idx, item in enumerate(sArray)}
    return ' '.join([dic[item] for itme in array])

print(soultion(int(input())))