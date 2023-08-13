def reverseDigits(number, reverse = 0):
    if number < 10:
        return reverse * 10 + number
    else:
        reverse = reverse * 10 + number % 10
        return reverseDigits(number // 10, reverse)


try:
    number = int(input('>>> Informe um número: '))
    print(f'O número {number} invertido vale {reverseDigits(number)}')
except Exception as exception:
    print('<ERRO>: O número deve ser inteiro.')
    print(exception)
