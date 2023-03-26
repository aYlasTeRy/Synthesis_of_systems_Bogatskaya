# https://new.contest.yandex.ru/41237/problem?id=149944/2022_10_13/qCXhJgNHI9

x = int(input())
n = int(input())
for i in range(n):
    s = input()
    if len(s) > x:
        for f in s:
            print(s[:x - 3] + '...')
            break
    else:
        print(s)