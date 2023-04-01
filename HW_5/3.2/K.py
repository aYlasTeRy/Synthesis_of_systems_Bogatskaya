# https://new.contest.yandex.ru/41238/problem?id=149944/2022_10_13/kqjNcEAgW2

text = [input() for item in range(int(input()))]
elements = set(text)
counter = 0
for item in elements:
    if text.count(item) != 1:
        counter += text.count(item)
print(counter)




