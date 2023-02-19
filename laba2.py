import numpy as np

size = int(input('Введите размер матрицы от 1 до 50: '))
while (size < 1) or (size > 50):
    size = int(input('Неверный размер матрицы. ' 
                     '\nВведите размер матрицы от 1 до 50: '))
t = int(input('Введите количество знаков после запятой в результате вычисления: '))

x = np.random.randint(50, size=(size, size))       # Задаём матрицу
rank = np.linalg.matrix_rank(x)                    # Вычисляем ранг
print("Матрица:\n", x)
print("Ранг матрицы: ", rank)

n = 2
cond, det_factorial, num_factorial = 1, 1, 1       # Задаём условие точности и факториал
summa, last_summa = 0, 0                           # Задаём сумму и "предыдущую" сумму

while abs(cond) > (0.1 ** t):               # Пока модуль разницы "предыдущей" суммы и суммы больше точности, крутимся в цикле
    last_summa += summa
    num_factorial = (n - 1) * n
    det_factorial *= (n - 1) * n            # Вычисляем факториал n члена последовательности
    summa += np.linalg.det(x * num_factorial) / det_factorial
    n += 1
    cond = abs(last_summa-summa)
    last_summa = 0

print('Сумма: ', summa)                     #Выводим сумму
