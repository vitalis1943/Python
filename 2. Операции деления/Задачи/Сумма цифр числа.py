# Пользователь вводит 3-х значное число. Нужно найти сумму его цифр и вывести ее на экран.
num = int(input())
print(num // 100 + num % 100 // 10  + num % 10)