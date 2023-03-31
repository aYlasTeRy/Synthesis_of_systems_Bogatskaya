# https://new.contest.yandex.ru/41237/problem?id=149944/2022_10_13/5vjFLZ1M9w

s = input().split()
p = int(input())
print(' '.join([str(int(i) ** p) for i in s]))