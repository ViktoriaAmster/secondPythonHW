#Реализуйте алгоритм перемешивания списка
import random


listOFNumbers = []

for _ in range(5):
    listOFNumbers.append(int(input('Введите число: ')))

print(listOFNumbers)
# random.shuffle(listOFNumbers)
# print(listOFNumbers)

#Вторая версия

secondList = []
helpList = [False, False, False, False, False]
while False in helpList:
    indexNumbers = random.randint(0, 4)
    if not helpList[indexNumbers]:
        secondList.append(listOFNumbers[indexNumbers])
        helpList[indexNumbers] = True

print(secondList)