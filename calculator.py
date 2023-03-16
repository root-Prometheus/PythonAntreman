def toplama(işlem):
    number = 0
    liste = []
    i = 0
    for element in işlem:
        if element >= '0' and element <= '9':
            for element in işlem:
                if element == ' ':
                    break
                else:
                    number = (number * 10) + int(element)
        liste.append(number)
        number = 0
    print(liste[0] + liste[1])

def çarpma(işlem):
    number = 0
    liste = []
    i = 0
    for element in işlem:
        if element >= '0' and element <= '9':
            for element in işlem:
                if element == ' ':
                    break
                else:
                    number = (number * 10) + int(element)
        liste.append(number)
        number = 0
    print(liste[0] * liste[1])

def çıkartma(işlem):
    number = 0
    liste = []
    i = 0
    for element in işlem:
        if element >= '0' and element <= '9':
            for element in işlem:
                if element == ' ':
                    break
                else:
                    number = (number * 10) + int(element)
        liste.append(number)
        number = 0
    print(liste[0] - liste[1])

def bölme(işlem):
    number = 0
    liste = []
    i = 0
    for element in işlem:
        if element >= '0' and element <= '9':
            for element in işlem:
                if element == ' ':
                    break
                else:
                    number = (number * 10) + int(element)
        liste.append(number)
        number = 0
    print(liste[0] / liste[1])

hesap = input("işlemi gir:")
for element in hesap:
    if element == '+':
        toplama(hesap)
    elif element == '-':
        çıkartma(hesap)
    elif element == '*':
        çarpma(hesap)
    elif element == '/':
        bölme(hesap)
