# https://new.contest.yandex.ru/41237/problem?id=149944/2022_10_13/OgIDCS3i0M

while True:
    s = input()
    if s == '':
        break
    if s.startswith('##') and s.endswith('@@@'):
        continue
    elif s.endswith('@@@'):
        continue
    elif s.startswith('##'):
        print(s[2:])
    else:
        print(s)