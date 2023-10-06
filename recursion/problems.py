# Slide 44-45
def tower_of_hanoi(disks = 3, origin = 'A', aux = 'B', destiny = 'C'):
    if disks:
        tower_of_hanoi(disks - 1, origin, destiny, aux)
        print(f'Movendo o disco {disks} de {origin} para {destiny}')
        tower_of_hanoi(disks - 1, aux, origin, destiny)


# Slide 46-48
def printBinaries(n):
    pass


# Slide 53
def biggestDigit(number):
    if number < 10:
        return number
    lastDigit = number % 10
    currentBiggestDigit = biggestDigit(number // 10)
    if lastDigit > currentBiggestDigit:
        return lastDigit
    return currentBiggestDigit


# Slide 53
def smallestDigit(number):
    if number < 10:
        return number
    lessSignificantDigit = number % 10
    currentSmallestDigit = smallestDigit(number // 10)
    if lessSignificantDigit < currentSmallestDigit:
        return lessSignificantDigit
    return currentSmallestDigit


# Slide 53
def countDigits(number):
    return 1 if number < 10 else 1 + countDigits(number // 10)


# Slide 53
def sumDigits(number):
    return number if number < 10 else number % 10 + sumDigits(number // 10)


# Slide 54
def resetEvenDigits(number):
    if number < 10:
        return number if number % 2 else 0
    elif number % 2:
        return resetEvenDigits(number // 10) * 10 + number % 10
    return resetEvenDigits(number // 10) * 10


# Slide 54
def resetOddDigits(number):
    if number < 10:
        return 0 if number % 2 else number
    elif number % 2:
        return resetOddDigits(number // 10) * 10
    return resetOddDigits(number // 10) * 10 + number % 10


# Slide 54
def removeEvenDigits(number):
    if number < 10:
        return number if number % 2 else 0
    elif number % 2:
        return removeEvenDigits(number // 10) * 10 + number % 10
    return removeEvenDigits(number // 10)


# Slide 54
def removeOddDigits(number):
    if number < 10:
        return 0 if number % 2 else number
    elif number % 2:
        return removeOddDigits(number // 10)
    return removeOddDigits(number // 10) * 10 + number % 10


# Slide 55
def reverseDigits(number, reverse = 0):
    if number == 0:
        return reverse
    return reverseDigits(number // 10, reverse * 10 + number % 10)


# Slide 56-58
def binarySearch(array, target, low, high):
    mid = (low + high) // 2
    if array[mid] == target:
        return True
    elif low == high or target < array[0] or target > array[len(array) - 1]:
        return False
    elif target < array[mid]:
        return binarySearch(array, target, low, mid - 1)
    return binarySearch(array, target, mid + 1, high)


# Slide 59
import unicodedata


def removeAccents(str):
    nfkd_form = unicodedata.normalize("NFKD", str)
    return "".join([c for c in nfkd_form if not unicodedata.combining(c)])


def hasMoreVowels(text, counter = 0, index = 0):
    text = removeAccents(text)
    if index == len(text):
        return counter > index / 2
    if text[index].lower() in 'aeiou':
        return hasMoreVowels(text, counter + 1, index + 1)
    return hasMoreVowels(text, counter, index + 1)


# Slide 59
def sort(array, k, index, lastIndex):
    if index > lastIndex:
        return array
    if array[index] <= k:
        return sort(array, k, index + 1, lastIndex)
    array.append(array.pop(index))
    return sort(array, k, index, lastIndex - 1)


# Slide 60
def twoIntEqualsTarget(array, target, low, high):
    if low > high:
        return False
    if array[low] + array[high] == target:
        return True
    if array[low] + array[high] > target:
        return twoIntEqualsTarget(array, target, low, high - 1)
    return twoIntEqualsTarget(array, target, low + 1, high)
