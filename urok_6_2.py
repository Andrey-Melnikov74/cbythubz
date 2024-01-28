print("Введите число X <= 2000000000 и нажмите Enter")
x = int(input())
b = 1
cnt = 0
for i in range(x):
    if (x % b == 0):
        cnt += 1
        b  += 1
    else:
        b  += 1
print(cnt, "количество натуральных делителей числа X (включая 1 и само число)")