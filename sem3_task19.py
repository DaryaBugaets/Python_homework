# Задача №19. Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность (сдвиг - циклический) 
# на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

# data=[int(i) for i in input("Введите числа: ").split()]
# print(data)

# вывести последнее число в списке
# data=[int(i) for i in input("Введите числа: ").split()]
# print(data[-1])

data=[int(i) for i in input("Введите числа: ").split()]
steps=int(input("Введите количество сдвигов: "))
steps=steps%len(data) 
data=[data[i-steps] for i in range(len(data))]
print(data)

