def twoIntEqualsTarget(array, target, low, high):
    if low > high:
        return False
    if array[low] + array[high] == target:
        return True
    if array[low] + array[high] > target:
        return twoIntEqualsTarget(array, target, low, high - 1)
    return twoIntEqualsTarget(array, target, low + 1, high)


array = [2, 7, 14, 15, 16, 20, 34, 28, 47, 49]
try:
    target = int(input('>>> Informe um número: '))
    print(twoIntEqualsTarget(array, target, 0, len(array) - 1))
except Exception as exception:
    print(exception)
