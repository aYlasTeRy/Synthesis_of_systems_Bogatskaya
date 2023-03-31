# https://new.contest.yandex.ru/41238/problem?id=149944/2022_10_13/DL6KYE4eaB

M = int(input())
N = int(input())
s1 = []
s2 = []
for i in range(M):
    s1.append(input())
for j in range(N):
    s2.append(input())

if len(set(s1) ^ set(s2)) == 0:
    print('Таких нет')
else:
    print(len(set(s1) ^ set(s2)))