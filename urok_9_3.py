print("Введите через пробел числа")
l = list(map(int, input().split()))
l.sort()
s1 = l[0:len(l):2]
s1_s = set(s1)
s2 = l[1:len(l):2]
s2_s = set(s2)
yes_s = s1_s.intersection(s2_s)
yes = list(yes_s)
no_s = s1_s.symmetric_difference(s2_s)
no = list(no_s)
for item in yes:
    print(item, end= ' YES\n')
for item in no:
    print(item, end= ' NO\n')
#print(*yes, sep= ' YES\n') # код короче, но не выводит "YES" в последней строке рядом с чилом
#print(*no, sep= ' NJ\n') # код короче, но не выводит "NO" в последней строке рядом с чилом


