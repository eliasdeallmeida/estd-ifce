def removeEvenDigits(number):
    if number < 10:
        return number if number % 2 else 0
    elif number % 2:
        return removeEvenDigits(number // 10) * 10 + number % 10
    return removeEvenDigits(number // 10)


try:
    number = int(input('>>> Informe um número: '))
    print(f'O número {number} com os dígitos pares removidos vale {removeEvenDigits(number)}')
except Exception as exception:
    print(exception)
