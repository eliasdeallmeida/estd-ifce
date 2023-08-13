def biggestDigit(number):
    if number < 10:
        return number
    else:
        lessSignificantDigit = number % 10
        currentBiggestDigit = biggestDigit(number // 10)
        if lessSignificantDigit > currentBiggestDigit:
            return lessSignificantDigit
        return currentBiggestDigit

try:
    number = int(input('>>> Informe um número: '))
    print(f'O maior dígito de {number} é {biggestDigit(number)}')
except Exception as exception:
    print('<ERRO>: O número deve ser inteiro.')
    print(exception)
