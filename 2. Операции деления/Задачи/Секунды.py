t = int(input('Кол-во секунд: '))
h = t // 3600
m = t % 3600 // 60
s = t % 60
print(f'{h}:{m}:{s}')
