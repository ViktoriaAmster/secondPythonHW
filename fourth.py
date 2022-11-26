#Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.

listOFSequence = []

while (number := int(input('Введите число: '))) < 1:
    print('Число должно быть больше 0! Повторите ввод!')

for i in range(-number, number+1):
    listOFSequence.append(i)

print(listOFSequence)
indices = input(f'Через пробел выведите номера индексов (с 0) для подсчета произведения: ').split(' ')
print(indices)
multipl = 1

#проверка на вхождение индексов в допустимы диапазон
while any((int(index) >= len(listOFSequence)) or (int(index) < 0) for index in indices): 
    indices = input(f'Числа должны быть от 0 до {len(listOFSequence)-1}: ').split(' ')
    print(indices)

for i in indices:
    multipl *= listOFSequence[int(i)]

print(f'Произведение элементов на этих индексах = {multipl}')