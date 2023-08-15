def reverseDigits(number, reverse = 0):
    if number == 0:
        return reverse
    return reverseDigits(number // 10, reverse * 10 + number % 10)


try:
    number = int(input('>>> Informe um número: '))
    print(f'O número {number} invertido vale {reverseDigits(number)}')
except Exception as exception:
    print(exception)
