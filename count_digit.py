def countDigits(number):
    return 1 if number < 10 else 1 + countDigits(number // 10)


try:
    number = int(input('>>> Informe um número: '))
    print(f'O número {number} tem {countDigits(number)} dígitos')
except Exception as exception:
    print('<ERRO>: O número deve ser inteiro.')
    print(exception)
