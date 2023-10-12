import unicodedata


# Slide 44-45
def tower_of_hanoi(disks=3, origin='A', aux='B', destiny='C'):
    if disks:
        tower_of_hanoi(disks - 1, origin, destiny, aux)
        print(f'Movendo o disco {disks} de {origin} para {destiny}')
        tower_of_hanoi(disks - 1, aux, origin, destiny)


# Slide 46-48
def print_binaries(n):
    pass


# Slide 53
def biggest_digit(number):
    if number < 10:
        return number
    last_digit = number % 10
    current_biggest_digit = biggest_digit(number // 10)
    if last_digit > current_biggest_digit:
        return last_digit
    return current_biggest_digit


# Slide 53
def smallest_digit(number):
    if number < 10:
        return number
    last_digit = number % 10
    current_smallest_digit = smallest_digit(number // 10)
    if last_digit < current_smallest_digit:
        return last_digit
    return current_smallest_digit


# Slide 53
def count_digits(number):
    return 1 if number < 10 else 1 + count_digits(number // 10)


# Slide 53
def sum_digits(number):
    return number if number < 10 else number % 10 + sum_digits(number // 10)


# Slide 54
def reset_even_digits(number):
    if number < 10:
        return number if number % 2 else 0
    elif number % 2:
        return reset_even_digits(number // 10) * 10 + number % 10
    return reset_even_digits(number // 10) * 10


# Slide 54
def reset_odd_digits(number):
    if number < 10:
        return 0 if number % 2 else number
    elif number % 2:
        return reset_odd_digits(number // 10) * 10
    return reset_odd_digits(number // 10) * 10 + number % 10


# Slide 54
def remove_even_digits(number):
    if number < 10:
        return number if number % 2 else 0
    elif number % 2:
        return remove_even_digits(number // 10) * 10 + number % 10
    return remove_even_digits(number // 10)


# Slide 54
def remove_odd_digits(number):
    if number < 10:
        return 0 if number % 2 else number
    elif number % 2:
        return remove_odd_digits(number // 10)
    return remove_odd_digits(number // 10) * 10 + number % 10


# Slide 55
def reverse_digits(number, reverse=0):
    if number == 0:
        return reverse
    return reverse_digits(number // 10, reverse * 10 + number % 10)


# Slide 56-58
def binary_search(array, target, low, high):
    mid = (low + high) // 2
    if array[mid] == target:
        return True
    elif low == high or target < array[0] or target > array[len(array) - 1]:
        return False
    elif target < array[mid]:
        return binary_search(array, target, low, mid - 1)
    return binary_search(array, target, mid + 1, high)


# Slide 59
def remove_accents(str):
    nfkd_form = unicodedata.normalize("NFKD", str)
    return "".join([c for c in nfkd_form if not unicodedata.combining(c)])


def has_more_vowels(text, counter=0, index=0):
    text = remove_accents(text)
    if index == len(text):
        return counter > index / 2
    if text[index].lower() in 'aeiou':
        return has_more_vowels(text, counter + 1, index + 1)
    return has_more_vowels(text, counter, index + 1)


# Slide 59
def sort(array, k, index, last_index):
    if index > last_index:
        return array
    if array[index] <= k:
        return sort(array, k, index + 1, last_index)
    array.append(array.pop(index))
    return sort(array, k, index, last_index - 1)


# Slide 60
def has_sum_equals_target(array, target, low, high):
    if low > high:
        return False
    if array[low] + array[high] == target:
        return True
    if array[low] + array[high] > target:
        return has_sum_equals_target(array, target, low, high - 1)
    return has_sum_equals_target(array, target, low + 1, high)
