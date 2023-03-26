# https://new.contest.yandex.ru/41237/problem?id=149944/2022_10_13/a4hvWnzaSa

n = int(input())
k = 0
for i in range(n):
    s = input()
    k += s.count('зайка')
print(k)