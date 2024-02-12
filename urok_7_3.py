
m = int(input("Введите число от 1 до 1000000000 (включительно), которое соответствует гузоподъемности одной лодки и нажмите 'Enter'", ))
n = int(input("Введите число от 1 до 100 (включительно), которое соответствует числу рыбаков и нажмите 'Enter'", ))
spisok_0 = [] #список рыбаков начальный
i = 0
for i in range(n):
    print("Введите число от 1 до", m," (включительно), которое соответствует массе рыбака и нажмите 'Enter'")
    a = int(input())
    spisok_0.append(a)
spisok_0.sort()
b = 0
cnt = 0
for i in range(n//2):
    if spisok_0[b] + spisok_0[-1] <= m:
        c = spisok_0[-1]
        spisok_0.insert(b+1, c)
        spisok_0.pop()
        cnt += 1
        b += 2
    else:
        c = spisok_0[-1]
        spisok_0.insert(b+1, c)
        spisok_0.pop()
print(n-cnt*2+cnt, "лодок (лодки) потребуется")