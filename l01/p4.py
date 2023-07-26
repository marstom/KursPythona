# kolejny typ danych lista, mutowalny typ danych

# to samo
lista = list()
lista2 = []

# concat
[1, 2, 3] + [4, 5, 6]

['a', 'b', 'c']

''.join(['a', 'b', 'c'])

# dozwolone?

['a', 'b', 12, 5.2]
['ala', ['a', 'b', 12, 5.2], [1, 2, ['abc']]]

# operacje
moja_lista = 'The quick brown fox jumps over the lazy dog'.split(' ')
lista = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
# po indeksie

liczby = [1, 2, 1, 4, 5, 1, 7, 8, 1]
# range
liczby2 = list(range(0, 20))
liczby2
liczby2[::2]
# na koniec
liczby2.append(22)
liczby2.append(44)
liczby2

# na początek
liczby2.insert(0, 999)
liczby2.insert(5, 888)
liczby2

# Zdejmujemy ze stosu
print(liczby2.pop())


# stack
stack = ['adam', 'tomek', 'celina', 'henry']
stack.pop()
stack.pop()

queue = ['adam', 'tomek', 'celina', 'henry']
queue.pop()
queue.pop()

# usuńmy 888
liczby2.remove(888)

# policzmy elementy
len(liczby2)

# minimum i maximum listy
print(min(liczby2), max(liczby2))

['a', 'b', 'c'] * 3

lista3 = ['hej', 'szukam', 'napisu', 'ABC', 'na', 'liście']
lista3.index('ABC')  # jest na indekise 3
lista3.index('qwer')  # jak czegoś nie ma rzuca wyjątek ValueError

# sortowanie
lista4 = ['ala', 'ma', 'kota']
lista4.sort()  # posortuje w miejscu
lista4

# nie zmienia oryginału
sorted(lista4)
lista4

id(lista4)

lista4.append('a')
id(lista4)

# lista4.copy()

# doda do mojej oryginalnej listy, bo jest id takie samo!
lista_pod_inna_zmienna = lista4
lista_pod_inna_zmienna.append('tomek')
print(f"moja lista:{id(lista4)} nowa lista: {id(lista_pod_inna_zmienna)}")
print(lista4)
print(lista_pod_inna_zmienna)

skopiowana_lista = lista4.copy()
skopiowana_lista.append('ASDF')
print(f"moja lista:{id(lista4)} skopiowana lista: {id(skopiowana_lista)}")
print(lista4)
print(lista_pod_inna_zmienna)
print(skopiowana_lista)  # to jest kopia, należy pamiętać o mutoalności list!

# Operator gwiazdka

lista = ['ala', 'ma']
liczby = [1, 2, 3, 4]

razem = [lista, liczby]
razem

razem = [*lista, *liczby]
razem

# funkcje

# sumowanie liczby na liście

l1 = [2, 5, 10]
sum(l1)

l2 = ['ala', 'ma', 'kota']
sum(l2)  # wyjątek, nie dozwolone, sum oczekuje liczby
' '.join(l2)  # tak można połączyć napisy

# iterowanie po liście, bardziej "pythonic"

for el in l2:
    print(el)

# albo tak-nie polecam
for i in range(len(l2)):
    print(f'element {i} to: {l2[i]}')

# albo bardziej "pythonic" można to zrobić
for idx, el in enumerate(l2):
    print(f'element {idx} to: {el}')

# słowo kluczowe break
for idx, el in enumerate(l2):
    print(f'element {idx} to: {el}')
    if el == 'ma':
        break  # przerywa pętlę, jeśli element listy jest równa ma

# słowo kluczowe continue
for idx, el in enumerate(l2):
    if el == 'ma':
        continue  # kontynuuj iteracje bez wykonywania kodu poniżej
    print(f'element {idx} to: {el}')

# funkcja builtin zip
l3 = ['ala', 'ma', 'kota']
l4 = ['ALA', 'MA', 'KOTA']

list(zip(l3, l4))

# filtrowanie
# lista = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
# list(filter(lambda x: len(x) <= 3, lista))
