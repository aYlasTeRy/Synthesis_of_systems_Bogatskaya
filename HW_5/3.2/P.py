# https://new.contest.yandex.ru/41238/problem?id=149944/2022_10_13/ki6S7TkGcp

element = set()
while True:
    text = input()
    if text == '':
        break
    for item in range(len(text.split())):
        if item == 0 and text.split()[item] == 'зайка':
            element.add(text.split()[item + 1])
        if item == len(text.split()) - 1 and text.split()[item] == 'зайка':
            element.add(text.split()[item - 1])
        if 0 < item < len(text.split()) - 1 and text.split()[item] == 'зайка':
            element.add(text.split()[item + 1])
            element.add(text.split()[item - 1])
for animal in element:
    print(animal)
