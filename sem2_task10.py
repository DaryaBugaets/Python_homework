# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, 
# которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и
# той же стороной. Выведите минимальное количество монет, 
# которые нужно перевернуть

n=int(input('Введите количество монет: '))
reshka=gerb=0
for i in range(n):   #цикл, который будет проходить по нашим значениям
    a=int(input('решка(1) или герб(0) '))
    if a ==1:
        reshka+=1
    else:
        gerb+=1

if reshka>gerb:
    output=gerb
else:
    output=reshka
print(f'Минимальное количество монет, которые нужно перевернуть {output}')