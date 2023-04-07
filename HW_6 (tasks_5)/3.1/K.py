# https://new.contest.yandex.ru/41237/problem?id=149944/2022_10_13/pKCFLSCyj7

data = []
for item in range(int(input())):
    data.append(input())
search = input()
for ch in data:
    if search.lower() in ch.lower():
        print(ch)