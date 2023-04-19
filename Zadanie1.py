# a = int(input('1 Введите кол-во учеников = '))
# b = int(input('2 Введите кол-во учеников = '))
# c = int(input('3 Введите кол-во учеников = '))
# s = a + b + c
# v = s / 2
# if v % 2 == 0:
#     print(v)
# else:
#     print(v + 0.5)

# a = int(input('1  = '))
# b = int(input('2  = '))
# c = int(input('3  = '))
# d = int(input('4  = '))
# if (a + b + c + d) == 0:
#     print('YES')
# else:
#     print('NO')

m = int(input('1  = '))
n = int(input('2  = '))
k = int(input('3  = '))
if k <= (n * m) and ((k % n == 0) or (k % m == 0)):
    print('YES')
else:
    print('NO')