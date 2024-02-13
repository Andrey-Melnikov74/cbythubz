a = input("введите слово ", )
print(a)
n = len(a)
if a[0:n-1:1] == a[n-1:0:-1]:
    print('yes')
else:
    print('no')