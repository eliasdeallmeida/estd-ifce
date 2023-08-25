def tower_of_hanoi(disks = 3, origin = 'A', aux = 'B', destiny = 'C'):
    if disks:
        tower_of_hanoi(disks - 1, origin, destiny, aux)
        print(f'Movendo o disco {disks} de {origin} para {destiny}')
        tower_of_hanoi(disks - 1, aux, origin, destiny)


try:
    disks = int(input('>>> Informe o número de discos: '))
    print(f'Quantidade mínima de jogadas: {2 ** disks - 1}')
    print(f'{"PASSO A PASSO":^25}')
    tower_of_hanoi(disks)
except Exception as exception:
    print(exception)
