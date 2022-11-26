#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

while (number:=int(input('Введите целое число больше ноля: '))) < 1:
    print('Число должно быть целым и больше ноля!')

factorial = 1
for i in range(1, number+1):
    factorial *= i

print(f'Факториал числа {number} = {factorial}')