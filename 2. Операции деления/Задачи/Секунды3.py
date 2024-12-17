f = int(input('Кол-во секунд'))
num1 = f//3600
num2 = (f%3600)//60
num3 = (f%3600)%60
print(num1,':',num2,':',num3)