def sort(array, k, index, lastIndex):
    if index > lastIndex:
        return array
    if array[index] <= k:
        return sort(array, k, index + 1, lastIndex)
    array.append(array.pop(index))
    return sort(array, k, index, lastIndex - 1)


array = [6, 1, 53, 12, 6, 18, 11, 21, 8, 2]
try:
    k = int(input('>>> Informe um valor para k: '))
    print(sort(array, k, 0, len(array) - 1))
except Exception as exception:
    print(exception)
