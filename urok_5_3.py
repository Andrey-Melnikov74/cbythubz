print("Введите через пробел: Стоимость стартапа, количество денег Майкла, количество денег Ивана")
a, b, c = map(float, input().split())
if (b >= a) and (c >= a):
    print(2)
else:
    if (b + c >= a) and  (b >= a):
        print("Mikle")
    else:
        if (b + c >= a) and  (c >= a):
            print("Ivan")
        else:
            if (b + c >= a):
                print(1)
            else:
                print(0)