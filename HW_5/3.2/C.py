# https://new.contest.yandex.ru/41238/problem?id=149944/2022_10_13/JnnhhAewGx

N = int(input())
s1 = []
for i in range(N):
    s1 += input().split()
print('\n'.join(set(s1)))