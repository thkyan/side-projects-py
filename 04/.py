import time

my_time = int(input('digite o tempo em segundos que deseja:'))

for x in range(my_time, 0, -1):
    segundos = x % 60
    minutos = int(x / 60) % 60
    horas = int(x / 3600)
    print(f'{horas}:{minutos:02}:{segundos:02}')
    time.sleep(1)

print('o tempo acabou')