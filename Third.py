#Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму

while (quantity := int(input('Введите число сколько элементов должно отображаться: '))) < 1:
    print('Число должно быть целое и больше ноля!')

listOfSequence = []
sum_ = 0

for i in range(1, quantity+1):
    listOfSequence.append(round((1+1/i)**i, 2))

for i in listOfSequence:
    sum_ += i
print(f'Последовательность из {quantity} чисел -{listOfSequence}')
print(f'Сумма всех элементов = {sum_}')
