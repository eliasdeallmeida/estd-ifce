def resetEvenDigits(number):
    if number < 10:
        return number if number % 2 else 0
    elif number % 2:
        return resetEvenDigits(number // 10) * 10 + number % 10
    return resetEvenDigits(number // 10) * 10


try:
    number = int(input('>>> Informe um número: '))
    print(f'O número {number} com os dígitos pares zerados vale {resetEvenDigits(number)}')
except Exception as exception:
    print(exception)
