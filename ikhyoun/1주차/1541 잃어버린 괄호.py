operate = input().split('-')
num = 0
for number in operate[0].split('+'):
    num += int(number)
    
for st in operate[1:]:
    for number in st.split('+'):
        num -= int(number)

print(num)