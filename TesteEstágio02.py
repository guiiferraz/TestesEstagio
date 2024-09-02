num = int(input('Digite um valor: '))
p1 = 0
p2 = 1
acumulador = 0

while True:
    p3 = p1 + p2
    if p3 == num:
        print(f'O numero {num} faz parte da sequência!')
        break
    elif p3 > num:
        print(f'O número {num} não faz parte da sequência!')
        break
    p1 = p2
    p2 = p3

