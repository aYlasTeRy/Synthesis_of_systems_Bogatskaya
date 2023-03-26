# https://new.contest.yandex.ru/41237/problem?id=149944/2022_10_13/vpdTAfe36G

n = int(input())
for i in range(n):
    s = input()
    if s.find('зайка') != -1:
        print(s.find('зайка') + 1)
    else:
        print('Заек нет =(')