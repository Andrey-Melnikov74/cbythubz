my_dict = {}
a = 0
while a == 0:
    b = int(input("Ввелите число", ))
    my_dict_1 = {b : b ** b}
    my_dict.update(my_dict_1)
    print(my_dict)
    a = int(input("продолжить - введите 0, завершить работу программы и получить результат - нажмите любую клавишу (кроме '0')", ))