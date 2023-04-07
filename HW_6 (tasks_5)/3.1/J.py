# https://new.contest.yandex.ru/41237/problem?id=149944/2022_10_13/fCcQ3iQzrD

count = 0
max_char = ''
while True:
    s = input().lower()
    if s == 'ФИНИШ':
        break
    for i in range(len(s)):
        if s.count(s[i]) >= count:
            count = s.count(s[i])
            max_char = s[i]
    print(max_char)