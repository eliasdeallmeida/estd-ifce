def binarySearch(array, target, low, high):
    mid = (low + high) // 2
    if array[mid] == target:
        return True
    elif low == high or target < array[0] or target > array[len(array) - 1]:
        return False
    elif target < array[mid]:
        return binarySearch(array, target, low, mid - 1)
    return binarySearch(array, target, mid + 1, high)


array = [1, 4, 5, 7, 8, 9, 10, 12, 15, 20, 45, 67]
print(array)
try:
    target = int(input('>>> Informe o número que deseja encontrar na sequência acima: '))
    print(f'O número {target}{"" if binarySearch(array, target, 0, len(array)) else " não"} está contido.')
except Exception as exception:
    print(exception)
