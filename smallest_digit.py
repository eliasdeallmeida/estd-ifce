def smallestDigit(number):
    if number < 10:
        return number
    lessSignificantDigit = number % 10
    currentSmallestDigit = smallestDigit(number // 10)
    if lessSignificantDigit < currentSmallestDigit:
        return lessSignificantDigit
    return currentSmallestDigit


try:
    number = int(input('>>> Informe um número: '))
    print(f'O menor dígito de {number} é {smallestDigit(number)}')
except Exception as exception:
    print(exception)
