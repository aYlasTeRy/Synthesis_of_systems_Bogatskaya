# https://new.contest.yandex.ru/41237/problem?id=149944/2022_10_13/8Ymb2732go

data = ['Манная', 'Гречневая', 'Пшённая', 'Овсяная', 'Рисовая']
for item in range(int(input())):
    print(data[item % 5])