def hasMoreVowels(text, vowels, counter = 0, index = 0):
    if index == len(text):
        return True if counter > index / 2 else False
    if text[index] in vowels:
        return hasMoreVowels(text, vowels, counter + 1, index + 1)
    return hasMoreVowels(text, vowels, counter, index + 1)


vowels = 'aeiouAEIOUáéíóúÁÉÍÓÚãõÃÕàèìòùÀÈÌÒÙäëïöüÄËÏÖÜ'
text = str(input('>>> Informe um texto qualquer: '))
print(f'O texto "{text}"{"" if hasMoreVowels(text, vowels) else " não"} tem mais vogais que consoantes.')
