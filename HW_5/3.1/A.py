# https://new.contest.yandex.ru/41237/problem?id=149944/2022_10_13/Rqerjkkkal

n = int(input())
count = 0
for i in range(n):
    s = input()
    for j in s:
        if s[0] == 'а' or s[0] == 'б' or s[0] == 'в':
            count += 1
        else:
            count += 0
        break
if count == n:
    print('YES')
else:
    print('NO')