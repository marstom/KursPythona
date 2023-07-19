#  komentarze
"""

Komentarz
blokowy
"""
from math import sqrt

print(3 + 5 + 6 * 3 // 2)
print(round(8 / 9, 4))

print(sqrt(9))

lista = ['jabłka', 'gruszki', 'chleb']
lista.append('jaja')
lista.append('majonez')
lista.append('ser')
lista.append('pietruszka')
lista.append('szynka')
print(lista)

print(', '.join(lista))


def myslniki(item):
    return '- ' + item + '\n'


print(''.join(map(myslniki, lista)))

# co trzeci el listy
print(lista[::3])
