def resetOddDigits(number):
    if number < 10:
        return 0 if number % 2 else number
    elif number % 2:
        return resetOddDigits(number // 10) * 10
    return resetOddDigits(number // 10) * 10 + number % 10


try:
    number = int(input('>>> Informe um número: '))
    print(f'O número {number} com os dígitos ímpares zerados vale {resetOddDigits(number)}')
except Exception as exception:
    print(exception)
