n = int(input("Введите число ноебходимиго количества чисел и нажмите 'Enter' ", ))
print("Введите через пробелы необходимое колличество чисел списка 1")
rjad_1 = set(map(int, input().split(" ")[:n])) #[:n] отсекает лишние числа, если они дыли введены
print("Введите через пробелы необходимое колличество чисел списка 2")
rjad_2 = set(map(int, input().split(" ")[:n])) #[:n] отсекает лишние числа, если они дыли введены
print(rjad_1) #вывод множества, если необходимо
print(rjad_2) #вывод множества, если необходимо
rjad_3 = rjad_1.intersection(rjad_2)
print(len(rjad_3))