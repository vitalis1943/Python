t = int(input('Кол-во секунд'))
num1 = t//3600
num2 = (t%3600)//60
num3 = (t%3600)%60
print(num1,':',num2,':',num3)