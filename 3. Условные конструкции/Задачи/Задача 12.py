m = int(input('Кол-во грибов: '))
if m%10 == 1 and m%100 != 11:
    print("гриб")
elif 1 < m%10 < 5 and 15 < m&100 < 11:
    print("гриба")
else:
    print("грибов")








