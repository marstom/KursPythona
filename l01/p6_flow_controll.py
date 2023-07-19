# zmienne bool

prawda = True
falsz = False

if prawda:
    print("Wyknano")

if falsz:
    print("Wyknano")

liczba = 1

if liczba == 0:
    print("Liczba jest zerem")
else:
    print("Liczba różna od zera")

liczba2 = 1

if liczba2 == 0:
    print("Liczba jest zerem")
elif liczba2 == 1:
    print("Liczba równa jeden")
elif liczba2 >= 2 and liczba2 <= 5:
    print("Liczba pomiędzy 2 a 5")
elif liczba2 > 5 and liczba2 <= 10:
    print("Liczba pomiędzy 6 a 10")
else:
    print("Liczba jest ujemna lub większa niż 10")

# operacje na bool
# and tylko jeśli wszystkie są prawdziwe
True and True
True and False
True and True and False

# or - przynajmniej jedno jset prawdą
True or False or False
False or False or False

# xor Alternatywa rozłączna, alternatywa wyłączająca, ekskluzja
True ^ False
False ^ True
True ^ True
False ^ False

# negacja
not True
not False

2 > 3
2 < 3
3 == 3
3 != 4  # różne
3 != 3

3 >= 3  # większe równe
3 <= 3  # większe równe

# == porównuje wartości
# is porównuje obiekty

[1, 2, 3] is [1, 2, 3]  # false bo różne id
[1, 2, 3] == [1, 2, 3]  # true bo te same wartości

# in sprawdza czy sekwencja jest w obiekcie

'kot' in 'ala ma kota'
'kot' in ['ala', 'ma', 'kota']  # false, porównuje cały string w liście
'kota' in ['ala', 'ma', 'kota']  # true, jest taki element
'kota' not in ['ala', 'ma', 'kota']  # false, sprawdzam czy nie ma takiego elementu - jest - czyli false

# operatory binarne
mask = 0b00000111  # maska bitowa
a = 0b00000101
print(f'{a:08b} {a}')
# a = mask ^ a
# negacja 3 bitów
a = ~a  # operator negacji
a = mask & a  # operator and
print(f'{a:08b} {a}')

# wykorzystanie warunków logicznych w listach, list comperhenison!
# składnia: newlist = [expression for item in iterable if condition == True]
# list comperhension!
lista = ['to', 'jest', 'list', 'compehenison', 'ab', 'costam']
[el for el in lista if len(el) <= 4]  # tworzy liste w miejscu

[el * 5 for el in [1, 2, 3, 4]]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
[el for el in fruits if "a" in el]

[el if el != "banana" else "orange" for el in fruits]

[el for el in range(60, 75)]

# any oraz all

# wszystkie wyrażenie muszą być prawdziwe
print(all([True, True, False, False]))  # False
print(all([True, True, True, True]))  # True

# co najmniej jedno musi być prawdą
print(any([True, True, False, False]))  # True
print(any([True, True, True, True]))  # True
print(any([False, False, False, True]))  # True
print(any([False, False, False, False]))  # False
