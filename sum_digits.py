def sumDigits(number):
    return number if number < 10 else number % 10 + sumDigits(number // 10)


try:
    number = int(input('>>> Informe um número: '))
    print(f'A soma dos dígitos do número {number} vale {sumDigits(number)}')
except Exception as exception:
    print('<ERRO>: O número deve ser inteiro.')
    print(exception)
