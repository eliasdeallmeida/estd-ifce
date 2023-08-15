def removeOddDigits(number):
    if number < 10:
        return 0 if number % 2 else number
    elif number % 2:
        return removeOddDigits(number // 10)
    return removeOddDigits(number // 10) * 10 + number % 10


try:
    number = int(input('>>> Informe um número: '))
    print(f'O número {number} com os dígitos ímpares removidos vale {removeOddDigits(number)}')
except Exception as exception:
    print(exception)
