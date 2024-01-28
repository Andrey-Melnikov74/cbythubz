print("Введите число A - начало диапалона и нажмите Enter")
a = int(input())
print("Введите число B >= A - окончание диапалона и нажмите Enter")
b = int(input())
cnt = a
while cnt <= b:
    cnt += 1
    if (a/2 != a - a//2):
        a  += 1
    else:
        print(a, end=" ")
        a  += 1