def soulution(operate):
    num = 0
    for number in operate[0].split('+'):
        num += int(number)
        
    for st in operate[1:]:
        for number in st.split('+'):
            num -= int(number)
    return num

print(soulution(input().split('-')))