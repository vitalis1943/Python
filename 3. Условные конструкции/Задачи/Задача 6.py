a = int(input())
b = int(input())
c = int(input())
h = max(a, b, c)
c1 = min(a, b ,c)
c2 = a + b + c - h - c1
if c1 + c2 <= h:
    print("Не существует")
elif c1**2 + c2**2 == h**2:
    print('Прямоугольный')
elif c1**2 + c2**2 < h**2:
    print("Тупоугольный")
elif c1**2 + c2**2 > h**2:
    print('Остроугольный')