# https://new.contest.yandex.ru/41237/problem?id=149944/2022_10_13/YOO7ZFJH4A

s = []
for i in range(int(input())):
    s.append(int(input()))
p = int(input())
print('\n'.join([str(int(i) ** p) for i in s]))