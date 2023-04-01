# https://new.contest.yandex.ru/41238/problem?id=149944/2022_10_13/s6Jxtvde9U

text = ([input() for item in range(int(input()))])
elements = dict()

for item in set(text):
    if text.count(item) != 1:
        elements[item] = text.count(item)
if len(elements) == 0:
    print('Однофамильцев нет')
else:
    for item in sorted(elements.keys()):
        print(f'{item} - {text.count(item)}')