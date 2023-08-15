def biggestDigit(number):
    if number < 10:
        return number
    lastDigit = number % 10
    currentBiggestDigit = biggestDigit(number // 10)
    if lastDigit > currentBiggestDigit:
        return lastDigit
    return currentBiggestDigit


try:
    number = int(input('>>> Informe um número: '))
    print(f'O maior dígito de {number} é {biggestDigit(number)}')
except Exception as exception:
    print(exception)
