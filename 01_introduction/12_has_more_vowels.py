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


text = str(input('>>> Informe um texto qualquer: '))
print(f'O texto "{text}"{"" if hasMoreVowels(text) else " não"} tem mais vogais que consoantes.')
