s = int(input('Кол-во секунд'))
num1 = s//3600
num2 = (s%3600)//60
num3 = (365%3600)%60
print(num1,':',num2,':',num3)
